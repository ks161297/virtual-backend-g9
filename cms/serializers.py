from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from rest_framework import serializers
from .models import PlatoModel, UsuarioModel
from django.conf import settings
# != 

class RegistroSerializer(serializers.ModelSerializer):
    # *** Forma 1 => Declarar el atributo modificando sus validaciones a nivel de modelos y poniendo nuevas validaciones.
    # password => serializer.CharField(write_only=True, required=True) 

    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        password = self.validated_data.get('password')
        nuevoUsuario = UsuarioModel(usuarioNombre = usuarioNombre, usuarioApellido = usuarioApellido, usuarioCorreo = usuarioCorreo, usuarioTipo = usuarioTipo)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario
    class Meta: 
        model = UsuarioModel
        # fields = '__all__'
        exclude = ['groups','user_permissions','is_superuser','last_login','is_active','is_staff']

        # *** Forma 2
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields  = '__all__'

class ImagenSerializer(serializers.Serializer):
    archivo = serializers.ImageField(max_length=20,  # Indica el máximo de carácteres en el nombre de un archivo
                                    use_url=True) # Si su valor es True, el valor de la URL será usado para mostrar el nombre del archivo. Default => False
    def save(self):
        archivo: InMemoryUploadedFile = self.validated_data.get('archivo')
        print(archivo.content_type) # ? - ¿Qué archivo es?
        print(archivo.name) # ? - ¿Cuál es el nombre del archivo? 
        print(archivo.size) # ? - ¿Qué tamaño tiene el archivo(bytes)?

        
        # ! Una vez usado el método read(), elimina información del archivo en la RAM
        ruta = default_storage.save(archivo.name, ContentFile(archivo.read()))
        return settings.MEDIA_URL + ruta