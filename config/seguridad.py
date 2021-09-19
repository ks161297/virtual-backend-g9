from sqlalchemy.sql.functions import user
from models.Usuario import UsuarioModel
from bcrypt import checkpw
from .conexion_bd import base_de_datos

class Usuario:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __str__(self):
        return "Usuario con el id='%s' y username ='%s'" % (self.id, self.username)  # ===> Similar a format. 

def autenticador(username, password):
    '''Función encargada de JWT de validar las credenciales, valida si son ingresados correctamente y luego valida si es el usuario'''
    if username and password:
        usuario = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioCorreo == username).first()
        if usuario:
            hash = bytes(usuario.usuarioPassword, 'utf-8')
            pwdBytes = bytes(password, 'utf-8')
            if checkpw(pwdBytes, hash) is True:
                print('Es el usuario :)')
                return Usuario(usuario.usuarioId, usuario.usuarioCorreo)
    return None



def identificador(payload):
    '''Función para que una vez el usuario envie la token y quiera realizar una petición a una ruta protegida, esta función será encargada de identificar a dicho usuario y devolver su información'''
    print(payload)
    usuarioId = payload.get('usuario').get('id')
    print(usuarioId)
    usuarioEncontrado = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioId == usuarioId).first()
    if usuarioEncontrado:
        return usuarioEncontrado.__dict__
    return None
