from datetime import timedelta, datetime
from flask import Flask, current_app, render_template, request, send_file
from flask_restful import Api
from config.conexion_bd import base_de_datos
from models.Usuario import UsuarioModel
from models.Tarea import TareaModel
from controllers.Usuario import (RegistroController, 
                                    UsuarioController,
                                    ResetearPasswordController)
from controllers.Tarea import TareasController
from flask_jwt import JWT
from config.seguridad import autenticador, identificador
from dotenv import load_dotenv
from os import environ, path, remove
from config.configuracion_jwt import manejo_error_JWT
from cryptography.fernet import Fernet
from json import loads
from re import search
from bcrypt import gensalt, hashpw, checkpw
from utils.patrones import PATRON_CORREO, PATRON_PASSWORD
from uuid import uuid4
from cloudinary import config
from cloudinary.uploader import upload, destroy


load_dotenv()

app = Flask(__name__)
api = Api(app)

config(
    cloud_name=environ.get('CLOUD_NAME'),
    api_key=environ.get('API_KEY'),
    api_secret=environ.get('API_SECRET')
)

# C O N F I G => las variables de conf del py flask DEBUG=TRUE, PORT=5000
# ENVIRONMENT = DEVELOPMENT
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = environ.get('JWT_SECRET') # ==> contraseña de la token
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=30) # ==> cambia fecha de expiración
app.config['JWT_AUTH_USERNAME_KEY'] = 'email' # ==> cambia el parametro donde se pide nombre de usuario
app.config['JWT_AUTH_URL_RULE'] = '/login' # ==> endpoint donde se hara autenticación
app.config['JWT_AUTH_HEADER_PREFIX'] = 'BEARER' # ==> cambia el prefijo 



jsonwebtoken = JWT(app=app, authentication_handler=autenticador, identity_handler=identificador)

jsonwebtoken.jwt_error_callback = manejo_error_JWT

base_de_datos.init_app(app)
# base_de_datos.drop_all(app=app)
base_de_datos.create_all(app=app)

@jsonwebtoken.jwt_payload_handler
def definir_payload(identity):
    # print(identity)
    # print (app.config)
    creation = datetime.utcnow()
    expiration = creation + current_app.config.get('JWT_EXPIRATION_DELTA')
    not_before_delta = creation+\
        current_app.config.get('JWT_NOT_BEFORE_DELTA')
    user = {
        "id": identity.id,
        "correo": identity.username
    }
    print(current_app.config.get('JWT_EXPIRATION_DELTA'))
    return {
        "iat":creation,
        "exp":expiration,
        "nbf":not_before_delta,
        "usuario": user,
    }


@app.route('/pruebas-jinja', methods=['GET'])
def prueba_jinja():
    productos=['manzana','pera','higo','pollo']
    personas = [{
        "nombre":"Marigrace",
        "sexo":"Femenino"
    },{
        "nombre":"Berly",
        "sexo":"Masculino"
    },{
        "nombre":"Maritza",
        "sexo":"Femenino"
    },{
        "nombre":"Christian",
        "sexo":"Masculino"
    },{
        "nombre":"Danitza",
        "sexo":"Femenino"
    },{
        "nombre":"Sussetty",
        "sexo":"Femenino"
    }]
    masculinos = []
    femeninas = []
    for persona in personas:
        if persona['sexo'] == 'Femenino':
            femeninas.append(persona)
        elif persona['sexo'] == 'Masculino':
            masculinos.append(persona)
    return render_template('pruebas.jinja', nombre='Marigrace', saludo ='Buenas noches',productos=productos, femeninas=femeninas, masculinos=masculinos)

@app.route('/change-password', methods=['GET', 'POST'])
def cambiar_password():
    if request.method == 'GET':
        # print(request.args)
        token = request.args.get('token')  # ==> sacamos la token de los query params
        fernet = Fernet(environ.get('FERNET_SECRET')) # ==> creamos la instancia de Fernet
        # desencriptamos la token
        try:
            resultado = fernet.decrypt(bytes(token, 'utf-8')).decode('utf-8')
            resultado = loads(resultado)
            fecha_caducidad = datetime.strptime(resultado.get(
                'fecha_caducidad'), '%Y-%m-%d %H:%M:%S.%f')
            print(fecha_caducidad)
            print(datetime.utcnow())
            fecha_actual = datetime.utcnow()
            if fecha_actual < fecha_caducidad:
                print('todavia hay tiempo')
                return render_template('change_password.jinja', correo=resultado['correo'])
            else:
                print('ya no hay tiempo')
                raise Exception('ya no hay tiempo')
                # return render_template('bad_token.jinja')

        except Exception as e:
            print(e)
            return render_template('bad_token.jinja')
    elif request.method == 'POST':
        print(request.get_json())
        email = request.get_json().get('email') # ==> Usuario segun su correo
        password = request.get_json().get('password')
        usuario = base_de_datos.session.query(UsuarioModel).filter(
            UsuarioModel.usuarioCorreo == email).first()
        if usuario is None:
            return {
                "message": "Usuario no existe"
            }, 400
        if search(PATRON_PASSWORD, password) is None: # ==> Validación de formato constraseña
            return {
                "message": "Contraseña muy debil, mínimo 6, debe contener al menos una mayúcula, una minúscula, un número y un caracter"
            }, 400
        password_bytes = bytes(password, 'utf-8') # ==> Se encripta la nueva contraseña
        nuevaPwd = hashpw(password_bytes, gensalt()).decode('utf-8')
        try:
            base_de_datos.session.query(UsuarioModel).filter(
                UsuarioModel.usuarioId == usuario.usuarioId).update({'usuarioPassword': nuevaPwd}) # ==> Método UPDATE

            base_de_datos.session.commit()
            return {
                "message": "Se cambio la contraseña exitosamente"
            }
        except Exception as e:
            print(e)
            return {
                "message": "Hubo un error al actualizar el usuario"
            }, 400

@app.route('/subir-archivo-servidor', methods=['POST'])
def subir_archivo_servidor():
    archivo = request.files.get('imagen')
    if archivo is None:
        return {
            "message": "Archivo no encontrado"
        }, 404
    print(archivo.filename)  # filename => retornara el nombre del archivo
    print(archivo.mimetype)  # mimetype => retornara el formato (tipo) del archivo
    nombre_inicial = archivo.filename # sacar el nombre del archivo
    extension = nombre_inicial.rsplit(".")[-1] # sacado su extension
    nuevo_nombre = str(uuid4())+'.'+extension  # genero un nuevo nombre del archivo
    archivo.save(path.join('media', nuevo_nombre)) # uso ese nombre para guardar el archivo
    return {
        "message": "archivo subido exitosamente",
        "content": {
            "nombre": nuevo_nombre
        }
    }, 201

@app.route('/multimedia/<string:nombre>', methods=['GET'])
def devolver_imagen_servidor(nombre):
    try:
        return send_file(path.join('media', nombre))
    except:
        return send_file(path.join('media', 'not_found.png'))
@app.route('/eliminar-archivo-servidor/<string:nombre>', methods = ['DELETE'])

def eliminar_imagen_servidor(nombre):
    try:
        remove(path.join('media', nombre))
    finally:
        # funciona si el try fue exitoso o si no lo fue, osea, siempre se va a ejecutar
        return {
            "message": 'ok'
        }, 204

@app.route('/subir-imagen-cloudinary', methods=['POST'])
def subir_imagen_cd():
    imagen = request.files.get('imagen')
    print(imagen)
    resultado = upload(imagen)
    return {
        "message": "Archivo subido exitosamente",
        "content": resultado
    }


@app.route('/eliminar-imagen-cloudinary/<string:id>', methods=['DELETE'])
def eliminar_imagen_cd(id):
    respuesta = destroy(id)
    return {
        "message": "Imagen eliminada exitosamente",
        "content": respuesta
    }
# ====> R U T A S <====
api.add_resource(RegistroController, '/registro')
# api.add_resource(LoginController, '/login')
api.add_resource(UsuarioController, '/usuario')
api.add_resource(TareasController, '/tareas')
api.add_resource(ResetearPasswordController, '/reset-password')


if __name__ == '__main__':
    app.run(debug=True)


