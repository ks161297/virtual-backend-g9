from sqlalchemy.sql import base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class PreparacionModel(base_de_datos.Model):

    __tablename__ = 'preparaciones'


    preparacionId = Column(type_=types.Integer, name='id', primary_key=True, autoincrement=True, unique=True)

    preparacionOrden = Column(type_=types.Integer, name='orden', default=1)

    preparacionDescripcion= Column(type_=types.Text, name='descripcion', nullable=False)

    # Relaciones
    # Parametro column => nombre tabla, columna. 
    # ONDELETE => indicar la acción del hijo(tabla fk) cuando se elimine registro FK
    # CASCADE => Eliminar el registro de recetas y los ligados a ellas.
    # DELETE => Se eliminar y se deja al FK con el mismo valor aunque ya no exista.
    # RESTRICT => Restringe y prohibe la eliminación de recetas que tengan preparaciones, se debe eliminar primero preparaciones y después receta.
    # NONE => eliminado y en las preparaciones setea el valor de la receta a NULL
    
    receta = Column(ForeignKey(column='recetas.id', ondelete='RESTRICT'),
    name='recetas_id', type_=types.Integer, nullable=False)

    def __str__(self):
        return self.preparacionDescripcion