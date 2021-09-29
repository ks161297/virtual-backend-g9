from django.test import client
from django.utils import datastructures
import requests
from rest_framework import request
from rest_framework.test import APITestCase
from .models import ClienteModel, ProductoModel

class ProductosTestCase(APITestCase):
    def setUp(self):
        ProductoModel(productoNombre='Producto 01',
                      productoPrecio=20.40,
                      productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 02',
                      productoPrecio=20.40,
                      productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 03',
                      productoPrecio=20.40,
                      productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 04',
                      productoPrecio=20.40,
                      productoUnidadMedida='UN').save()

    def test_post_fail(self):
        '''Debería fallar el test cuando no se le pase la información '''
        print (self.shortDescription())
        request = self.client.post('/gestion/productos/')
        message = request.data.get('message')
        
        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Error al guardar el producto')
    
    def test_post_sucess(self):
        '''Deberia retornar el producto creado'''
        print(self.shortDescription())
        request = self.client.post('/gestion/productos/', data={
            "productoNombre":"Cartulina Canson Blanca",
            "productoPrecio": 1.50,
            "productoUnidadMedida": "UN"
        }, format='json')
        message = request.data.get('message')
        id = request.data.get('content').get('productoId')
        print(id)
        productoEncontrado = ProductoModel.objects.filter(productoId = id).first()

        self.assertEqual(request.status_code, 201)
        self.assertEqual(message, 'Producto creado exitosamente')
        self.assertIsNotNone(productoEncontrado)

    def test_get_success(self):
        '''Debería retornar los productos almacenados'''
        productoEncontrado = ProductoModel.objects.all()
        request = self.client.get('/gestion/productos/',data={'pagina': 1, 'cantidad': 2})
        print(request.data)
        paginacion = request.data.get('paginacion')
        content = request.data.get('data').get('content')
        self.assertIsNone(paginacion.get('paginaPrevia'))
        self.assertIsNotNone(paginacion.get('paginaContinua'))
        self.assertEqual(paginacion.get('porPagina'), 2)
        self.assertEqual(len(content), 2)
      

class ClienteTestCase(APITestCase):
    def setUp(self):
        ClienteModel(clienteNombre = 'SILVA SALAS MARIGRACE KIMBERLY STEFANIA', clienteDocumento='72750134', clienteDireccion='Mz M Lote 33 Cayma').save
    
    def test_post_cliente_fail(self):
        '''Debería lanzar error si los datos no son dados'''
        request = self.client.post('/gestion/clientes/')
        self.assertEqual(request.status_code, 400)

    def test_post_cliente_success(self):
        '''Debería crear el cliente y devolverlo'''
        nuevoCliente = {
            "clienteDocumento":"72750134",
            "clienteDireccion":"Mz M Lote 33 Cayma"
        }
        request = self.client.post('/gestion/clientes/', data=nuevoCliente, format='json')
        self.assertEqual(request.data.get('content').get('clienteDocumento'),
                        nuevoCliente.get('clienteDocumento'))

    def test_post_client_exists_fail(self):
        '''Debería lanzar un error si el cliente ya existe'''
        nuevoCliente = {
            "clienteDocumento":"72750134",
            "clienteDireccion":"Mz M Lote 33 Cayma"
        }
        self.client.post('/gestion/clientes/', data=nuevoCliente, format='json')
        request = self.client.post('/gestion/clientes/', data=nuevoCliente, format='json')
        self.assertEqual(request.status_code,400)