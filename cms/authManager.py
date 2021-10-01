from django.contrib.auth.models import BaseUserManager #Sirve para modificar el comportamiento de la creación de un usuario por consola. Nos permite modifica POR COMPLETO el modelo auth
# UserManager => Nos permite modificar campos como el firstName y lastname, agregar nuevos campos 

class ManejoUsuarios(BaseUserManager):
    def create_user(self, email, nombre, apellido, tipo, password = None):
        """Creación de un usuario"""
        if not email:
            raise ValueError('El usuario tiene que tener un correo válido')
        
       
        email = self.normalize_email(email)  # Validación de correo, normalizo haciéndolo todo en minúsculas. 
        
        # Creación de instancia del usuario
        usuarioCreado = self.model(usuarioCorreo = email, usuarioNombre = nombre, 
                                   usuarioApellido = apellido, usuarioTipo=tipo)
       
        usuarioCreado.set_password(password)  # set_password() => encriptar la contraseña
        usuarioCreado.save(using=self._db) # Sirva oara referencia a que base de datos se está haciendo la creación, esto se utiliza para cuando hay múltiples bases de datos en el py

        return usuarioCreado
    
    def create_superuser(self,usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password):
        '''Creación de un super usuario - administrador'''
        # *** Los parámetros que recibe tiene que ser los mismos que huvbiesemos declarado en el usuarioModel REQUIRED_FIELD y en el USERNAME_FIELD, llegarán con esos mismo nombre de parámetros y en el caso se escribiese mal, lanzará argumento inesperado
        nuevoUsuario = self.create_user(usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password)
        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True
        nuevoUsuario.save(using=self._db)  