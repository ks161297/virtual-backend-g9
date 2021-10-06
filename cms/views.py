from django.conf import settings
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ImagenSerializer, PlatoSerializer, RegistroSerializer, VentaSerializer
from .models import DetallePedidoModel, PedidoModel, PlatoModel, UsuarioModel
from rest_framework import status
from os import remove
from django.db import transaction

class RegistroController(CreateAPIView):

    serializer_class = RegistroSerializer
    def post(self, request:Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                'message':'Usuario creado correctamente',
                'content':data.data
            })
        else:
            return Response(data={
                'message':'Error al crear el usuario',
                'content':data.errors
            })

class PlatosController(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = PlatoModel.objects.all()
    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                'message':'Plato creado exitosamente',
                'content':data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al crear el plato',
                'content':data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response(data={
            'message':None,
            'content':data.data
        })
       
class SubirImagenController(CreateAPIView):
    serializer_class = ImagenSerializer
    def post(self, request: Request):
        data = self.serializer_class(data=request.FILES)
        if data.is_valid():
            archivo = data.save()
            url = request.META.get('HTTP_HOST')
            return Response(data={
                'message':'Archivo subido exitosamente',
                'content': url + archivo
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al subir el archivo',
                'content':data.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class PlatoController(RetrieveUpdateDestroyAPIView):
    serializer_class = PlatoSerializer
    queryset = PlatoModel.objects.all()

    def patch(self, request,id):
        ... #TAREA - ACTUALIZACIÓN PARCIAL
        platoEncontrado = PlatoModel.objects.filter(platoId=id).first()
        if platoEncontrado is None:
            return Response(data={
                'message':'Plato no existe',
                'content':None
            }, status=status.HTTP_404_NOT_FOUND)
        serializador = PlatoSerializer(platoEncontrado, data=request.data, partial=True)
        if serializador.is_valid():
            serializador.save()
            return Response(data={
                'message':'Éxito'
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al actualizar el plato',
                'content':serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    
    
    def put(self, request:Request, id):
        ... #TAREA - HACER EL PUT ACTUALIZACION TOTAL
        platoEncontrado = PlatoModel.objects.filter(platoId=id).first()
        if platoEncontrado is None:
            return Response(data={
                'message':'Plato no existe',
                'content':None
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = PlatoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=platoEncontrado, validated_data= serializador.validated_data)
            return Response(data={
                'message':'Plato actualizado con exito',
                'content':serializador.data
            })
        else:
            return Response(data={
                'message':'Error al actualizar el plato',
                'content':serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
    
    def get (self, request, id):
        platoEncontrado = self.get_queryset().filter(platoId=id).first()
        if not platoEncontrado:
            return Response(data={
                'message':'Plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        data = self.serializer_class(instance=platoEncontrado)
        return Response(data={
            'content':data.data
        })
        
    def delete (self, request, id):
        platoEncontrado = self.get_queryset().filter(platoId=id).first()
        if not platoEncontrado:
            return Response(data={
                'message':'Plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            data = platoEncontrado.delete()
            remove(settings.MEDIA_ROOT / str(platoEncontrado.platoFoto)) # Ubicacion archivo        
        
        except Exception as e:
            print(e)
            
        return Response(data={
            'message':'Plato eliminado exitosamente',
            'content': data
        })
# ! Prueba Kim :) 
# class DetallePedidoController(CreateAPIView):
#     serializer_class = PedidoSerializer
#     def post(self, request:Request):
#         data = self.serializer_class(data=request.data)
#         if data.is_valid():
#             idCliente = data.validated_data.get('cliente')
#             idVendedor = data.validated_data.get('vendedor')
#             clienteEncontrado = UsuarioModel.objects.filter(usuarioId = idCliente).filter(usuarioTipo = 3).first()
#             vendedorEncontrado = UsuarioModel.objects.filter(usuarioId = idVendedor).filter(usuarioTipo = 2).first()
#             detalles = data.validated_data.get('detalle')
    
#             try:
#                 with transaction.atomic():
#                     if clienteEncontrado is None or vendedorEncontrado is None:
#                         raise Exception('No existe')
                    
#                     nuevoPedido = PedidoModel(cliente = clienteEncontrado, vendedor=vendedorEncontrado)
#                     nuevoPedido.save()
#                     for detalle in detalles:
#                         plato = PlatoModel.objects.get(platoId=detalle.get('plato'))
#                         DetallePedidoModel(detalleCantidad=detalle.get('cantidad'), detalleSubTotal=plato.platoPrecio * detalle.get('cantidad'), plato=plato, pedido=nuevoPedido).save()
#             except Error as e:
#                 print(e)
#                 return Response(data={
#                     'message':'Error al crear el pedido',
#                     'content':e.args
#                 })
#             except Exception as exc:
#                 return Response(data={
#                     'message':'Error al crear el pedido',
#                     'content':exc.args
#                 })
#             return Response(data={
#                 'message':'Operacion registrada con exito',
#                 'content':data.data
        
#             },status=status.HTTP_201_CREATED)
#         else: 
#             return Response(data={
#                 'message':'Error al crear la operacion',
#                 'content': data.errors
#             }, status=status.HTTP_400_BAD_REQUEST)

class VentaController(CreateAPIView):
    serializer_class = VentaSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            cliente_id = data.validated_data.get('cliente_id')
            vendedor_id = data.validated_data.get('vendedor_id')
            detalles = data.validated_data.get('detalle')
            try:
                with transaction.atomic():
                    cliente = UsuarioModel.objects.filter(
                        usuarioId=cliente_id).first()

                    vendedor = UsuarioModel.objects.filter(
                        usuarioId=vendedor_id).first()

                    if not cliente or not vendedor:
                        raise Exception('Usuarios incorrectos')

                    if cliente.usuarioTipo != 3:
                        raise Exception('Cliente no corresponde el tipo')

                    if vendedor.usuarioTipo == 3:
                        raise Exception('Vendedor no corresponde el tipo')

                    pedido = PedidoModel(
                        pedidoTotal=0, cliente=cliente, vendedor=vendedor)

                    pedido.save()
                    for detalle in detalles:
                        plato_id = detalle.get('producto_id')
                        cantidad = detalle.get('cantidad')
                        plato = PlatoModel.objects.filter(
                            platoId=plato_id).first()
                        if not plato:
                            raise Exception('Plato {} no existe'.format(
                                plato_id))
                        if cantidad > plato.platoCantidad:
                            raise Exception(
                                'No hay suficiente cantidad para el producto {}'.format(plato.platoNombre))
                        plato.platoCantidad = plato.platoCantidad - cantidad
                        plato.save()
                        detallePedido = DetallePedidoModel(detalleCantidad=cantidad,
                                                           detalleSubTotal=plato.platoPrecio * cantidad,
                                                           plato=plato,
                                                           pedido=pedido)
                        detallePedido.save()
                        pedido.pedidoTotal += detallePedido.detalleSubTotal
                        pedido.save()
                return Response(data={
                    'message': 'Venta agregada exitosamente'
                })

            except Exception as e:
                return Response(data={
                    'message': e.args
                }, status=400)

        else:
            return Response(data={
                'message': 'Error al agregar la venta',
                'content': data.errors
            })

# ! Prueba Kim :) 
# class DetallesController(RetrieveAPIView):
#     serializer_class = PedidoModelSerializer
#     def get(self, request:Request, id):
#         inicial = get_object_or_404(PedidoModel, pk=id)
#         serializador = self.serializer_class(instance=inicial)
#         return Response(data={
#             'message':'El pedido es:',
#             'content':serializador.data
#         })


