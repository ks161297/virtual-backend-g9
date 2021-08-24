class Persona: 
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def saludar(self):
        print(f"Hola {self.nombre}")

    def __str__(self):
        """Método que sirve para que cuando vayamos a llamar a imprimir el objeto,se modifique por algo más entendible."""
        return self.nombre + " Instancia del objeto"

persona1 = Persona("Marigrace", "16-12-1997")
persona2 = Persona("Julián", "26-08-2014") 

print(persona1.nombre)
persona1.saludar()
persona2.saludar()

print(persona1)
print(persona2)