from enum import auto
from sqlalchemy.sql import base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class RecetaIngredienteModel(base_de_datos.Model):

    __tablename__ = 'recetas_ingredientes'

    recetaIngredienteId = Column( type_=types.Integer, primary_key=True, nullable=True, autoincrement=True, name='id')

    recetaIngredienteCantidad = Column( name='cantidad', type_=types.String(length=20), nullable=False)

   
    # Relaciones
    
    receta = Column(ForeignKey(column='recetas.id'), name='recetas_id', nullable=False, type_=types.Integer)

    ingrediente = Column(ForeignKey(column='ingredientes.id'), name='ingredientes_id', nullable=False, type_=types.Integer)