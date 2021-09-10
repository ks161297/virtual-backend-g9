from flask import Flask
from flask_restful import Api
from config.conexion_bd import base_de_datos
from dotenv import load_dotenv
from os import environ
# from models.usuario import UsuarioModel
# from models.tarea import TareaModel

from controllers.usuario import RegistroController
from controllers.LoginController import LoginController



load_dotenv()


app = Flask(__name__)
api = Api(app)
# CONFIG => las variables de configuración de mi py flask DEBUG = TRUE , PORT = 5000, ENVIROMENT = DEVELOPMENT

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)
base_de_datos.create_all(app=app)


#Rutas 
api.add_resource(RegistroController, '/registro')

api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)

