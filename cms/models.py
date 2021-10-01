from django.db import models
from .authManager import ManejoUsuarios
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import MinValueValidator

class PlatoModel(models.Model):
    platoId = models.AutoField(primary_key=True, null=False, db_column='id', unique=True)
    platoNombre = models.CharField(max_length=100, db_column='nombre', null=False)
    platoPrecio = models.DecimalField(db_column='precio', max_digits=5, decimal_places=2, null=False)

    # Almcenamiento de imágenes en el servidor.
    # A diferencia del FileField  el imagenField solamente permitirá el guardado de archivos con extensión(.jpg, .png, .svg, .jpeg)

    platoFoto = models.ImageField(upload_to='platos/', db_column='foto', null=False)
    platoCantidad = models.IntegerField(db_column='cantidad', null=False, default=0) 

    updateAt = models.DateTimeField(db_column='updated_at', auto_now=True) # Se actualizará su valor cuando el registro sufra alguna modificación.
                                                          # auto_now => Agarrará la fecha actual cuando parte del registro o en su totalidad sea modificacda.  

    created_At = models.DateTimeField(db_column='created_at', auto_now_add=True)
                                                            # auto_now_add => Cuando se cree un nuevo registro, agarrará la fecha actual y lo creará en la columna. 

    class Meta: 
        db_table = 'platos'

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = [(1, 'ADMINISTRADOR'), (2, 'MOZO'), (3,'CLIENTE')]

    usuarioId = models.AutoField(primary_key=True, db_column='id', unique=True, null=False)
    usuarioNombre = models.CharField(max_length=50, db_column='nombre')
    usuarioApellido = models.CharField(max_length=50, db_column='apellido')
    usuarioCorreo = models.EmailField(max_length=50, db_column='email', unique=True)
    usuarioTipo = models.IntegerField(choices=TIPO_USUARIO, db_column='tipo')
    password = models.TextField(null=False)
    
    # <> Campos BD modelo auth <>

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # <> INGRESAR UN ADMINISTRADOR POR CONSOLA: <>
     
    objects = ManejoUsuarios() # Agregamos el comportamiento cuando se llame a CREATESUPERUSER y al CREATE USER.

    USERNAME_FIELD = 'usuarioCorreo' # Se define la columna que será encargada de validar que el usuario sea único e irrepetible. 

    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido', 'usuarioTipo'] # Es lo que pedirá la consola cuando se llame al createsuperuser

    class Meta:
        db_table = 'usuarios'

class PedidoModel(models.Model):
    pedidoId = models.AutoField(primary_key=True, null=False, db_column='id', unique=True)
    pedidoFecha = models.DateTimeField(auto_now_add=True, db_column='fecha')
    pedidoTotal = models.DecimalField(max_digits=5, decimal_places=2, db_column='total')

    cliente =  models.ForeignKey(to=UsuarioModel, related_name='clientePedidos', db_column='cliente_id', on_delete=models.PROTECT)
    vendedor = models.ForeignKey(to=UsuarioModel, related_name='vendedorPedidos', db_column='vendedor_id', on_delete=models.PROTECT)

    class Meta:
        db_table = 'pedidos'

class DetallePedidoModel(models.Model):
    detalleId = models.AutoField(db_column='id', primary_key=True, unique=True, null=False)
    detalleCantidad = models.IntegerField(db_column='cantidad', null=False, validators=[MinValueValidator(0, 'Valor no puede ser negativo')])
    detalleSubTotal = models.DecimalField(max_digits=5, decimal_places=2, db_column='sub_total', null=False)

    # *** R E L A C I O N E S 

    plato = models.ForeignKey(to=PlatoModel, db_column='plato_id', related_name='platoDetalle', null=False, on_delete=models.PROTECT)
    pedido = models.ForeignKey(to=PedidoModel, db_column='pedido_id', related_name='pedidoDetalle', null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'detalles'