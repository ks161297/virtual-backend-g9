from rest_framework.fields import ImageField
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ImagenSerializer, PlatoSerializer, RegistroSerializer
from .models import PlatoModel
from rest_framework import status
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

class PlatoController(CreateAPIView):
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
