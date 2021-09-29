from rest_framework import serializers
from .models import CabeceraModel, ClienteModel, DetalleModel, ProductoModel

class ProductoSerializer(serializers.ModelSerializer):
    # productoNombre = serializers.DateTimeField()
    class Meta:
        model = ProductoModel
        fields= '__all__'
        # exclude = ['productoId']
class ClienteSerializer(serializers.ModelSerializer):
    clienteNombre = serializers.CharField(max_length=50, required=False, trim_whitespace = True, read_only=True)
    clienteDireccion = serializers.CharField(max_length=100, required=False, trim_whitespace = True)
    class Meta:
        model = ClienteModel
        fields = '__all__'

class DetalleOperacionSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(required=True, min_value=1)
    importe = serializers.DecimalField(max_digits=5, decimal_places=2, min_value=0.01, required=True)
    producto = serializers.IntegerField(required=True, min_value=1)



class OperacionSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(
        choices=[('V','VENTA'),('C','COMPRA')], required=True)
    
    cliente = serializers.CharField(required=True, min_length=8, max_length=11)
    detalle = DetalleOperacionSerializer(many=True)
    # detalle2 = serializers.ListField(child=DetalleOperacionSerializer)
class DetalleOperacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleModel
        exclude = ['cabeceras']
        # fields = '__all__'
        depth = 1

class OperacionModelSerializer(serializers.ModelSerializer):
    cabeceraDetalles = DetalleOperacionModelSerializer(many=True)
    class Meta:
        model = CabeceraModel
        fields = '__all__'
        depth = 1