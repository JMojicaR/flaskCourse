class Persona():
    texto = ''
    def __init__(self, nombre):
        self.nombre = nombre
        pass
    def saludar(self):
        self.texto = f'Hola mi nombre es {self.nombre}'
        return self.texto
    

persona1 = Persona("Antonio")

print(persona1.nombre)
texto = persona1.saludar()
print(texto)

class Adulto(Persona):
    def __init__(self,nombre):
        Persona.__init__(self,nombre)

adulto1 = Adulto('Juan')
texto1 = adulto1.saludar()
print(texto1)