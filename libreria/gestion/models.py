from django import db
from django.db import models

# https://docs.djangoproject.com/en/3.2/ref/models/
# https://docs.djangoproject.com/en/3.2/topics/db/models/

class ProductoModel(models.Model):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types  ==> Tipos de datos ORM
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options ==> 
    productoId = models.AutoField(primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(max_length=45, db_column='nombre', null=False)