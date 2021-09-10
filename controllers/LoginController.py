
from bcrypt import checkpw
from models.usuario import UsuarioModel
from flask_restful import Resource, reqparse
from config.conexion_bd import base_de_datos

class LoginController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'correo',
        type=str,
        required=True,
        location='json',
        help = 'Falta el correo'
    )
    serializador.add_argument(
        'password',
        type=str,
        required=True,
        location='json',
        help = 'Falta el password'
    )

    def post(self):
        # Si el usuario existe en la BD indicarlo si no en un mensaje que no exista
        data = self.serializador.parse_args()
        usuario = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioCorreo == data.get('correo')).first()
        if usuario is None:
             return {
                 "message" : "Usuario no encontrado"
             }, 404
        password = bytes(data.get('password'), ' utf-8')
        usuarioPwd = bytes(usuario.usuarioPassword,'utf-8')
        print(checkpw(password, usuarioPwd))
        return{
            "message": "Usuario encontrado"
        }