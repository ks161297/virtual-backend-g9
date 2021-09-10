
from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel
from config.conexion_bd import base_de_datos

#Hashear contraseña
from bcrypt import hashpw, gensalt, checkpw
from re import search


PATRON_CORREO = r'\w+[@]\w+[.]\w{2,3}'
PATRON_PASSWORD = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}'

class RegistroController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'nombre',
        type=str,
        location = 'json',
        required=True,
        help='Falta el nombre'
    )

    serializador.add_argument(
        'apellido',
        type=str,
        location = 'json',
        required=True,
        help='Falta el apellido'
    )

    serializador.add_argument(
        'correo',
        type=str,
        location = 'json',
        required=True,
        help='Falta el correo'
    )

    serializador.add_argument(
        'password',
        type=str,
        location = 'json',
        required=True,
        help='Falta el password'
    )

    serializador.add_argument(
        'telefono',
        type=str,
        location = 'json',
        required=True,
        help='Falta el telefono'
    )


    def post(self):
        data = self.serializador.parse_args()
        print(data)
        correo = data['correo']
        password = data['password']
        if search(PATRON_CORREO, correo) is None:
            return { 
                "message" : "Correo incorrecto"
            },400
        if search(PATRON_PASSWORD, password) is None:
            return { 
                "message" : "Password incorrecto, mínimo 6 caracteres, una mayúscula, una minúscula y un símbolo especial "
            }, 400
        try:
            nuevoUsuario = UsuarioModel()
            nuevoUsuario.usuarioCorreo=correo
            nuevoUsuario.usuarioNombre=data.get('nombre')
            nuevoUsuario.usuarioTelefono=data.get('telefono')
            nuevoUsuario.usuarioApellido=data.get('apellido')
            #Encriptación de la contraseña 
                #Primero se convierte a Bytes
            passwordBytes = bytes(password, "utf-8")
            # print(passwordBytes)
                # Llamamos al gensalt que nos dara un salt aleatorio en base al numero de rounds
            salt= gensalt(rounds=10)
                # hashpwd combina nuestras pwd 
            hashPwd = hashpw(passwordBytes,salt)
            hashPwd = hashPwd.decode('utf-8')
            nuevoUsuario.usuarioPassword = hashPwd
            base_de_datos.session.add(nuevoUsuario)
            base_de_datos.session.commit()
            print(hashPwd)
            return {
                "message" : "Usuario creado exitosamente"
             }, 201
        except Exception as e:
            base_de_datos.session.rollback()
            return {
                "message" : "Error al ingresar el usuario",
                "content" : e.args
             }, 500
           