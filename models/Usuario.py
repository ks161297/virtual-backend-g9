from enum import Flag

from sqlalchemy.sql.expression import null
from config.conexion_bd import base_de_datos
from sqlalchemy import Column, orm, types


class UsuarioModel(base_de_datos.Model):
    __tablename__ = 'usuarios'

    usuarioId = Column(name='id', type_=types.Integer, 
                        primary_key=True, nullable=False, autoincrement=True)
    usuarioNombre = Column(name='nombre', type_=types.String(50), nullable=False)
    usuarioApellido = Column(name='apellido', type_=types.String(50), nullable=False)
    usuarioTelefono = Column(name='telefono', type_=types.String(15), nullable=True)
    usuarioCorreo = Column(name='correo', type_=types.Text, nullable=False, unique=True)
    usuarioPassword = Column(name='password', type_=types.Text, nullable=False)
    
    tareas = orm.relationship('TareaModel', backref='tareaUsuario')