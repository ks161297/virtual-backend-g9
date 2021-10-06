from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include('cms.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
                           # document_root => Contenido que renderiza cuando llama a una ruta determinada con nombre de archivo.
