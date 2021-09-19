from enum import auto
from sqlalchemy.sql import base
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from config.conexion_bd import base_de_datos
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, types
from datetime import datetime
from enum import Enum

class EstadoEnum(Enum):
    POR_HACER = 'por_hacer'
    HACIENDO = 'haciendo'
    FINALIZADO = 'finalizado'

class TareaModel(base_de_datos.Model):
    __tablename__ = 'tareas'

    tareaId = Column(name='id', type_=types.Integer, autoincrement=True, primary_key=True)
    tareaTitulo = Column(name='titulo', type_=types.String(100), nullable=False)
    tareaDescripcion = Column(name='descripcion', type_=types.Text)
    tareaFechaCreacion = Column(name='created_at', type_=types.DateTime, default=datetime.now)
    tareaTags = Column(name='tags', type_=types.ARRAY(types.Text))
    tareaEstado = Column(name='estado', type_=types.Enum(EstadoEnum), nullable=False)
    tareaImagen = Column(name='imagen', type_=types.Text, nullable=True)



    # ====> R E L A C I O N E S  <=====

    usuario = Column(ForeignKey(column='usuarios.id'), name='usuario_id', type_=types.Integer, nullable=False)