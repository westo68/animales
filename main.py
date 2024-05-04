import datetime


class animal:
    jugar = False

    def __init__(self, raza: str, f_nacimiento: datetime, f_ingreso: datetime):#input con tipo de dato
        self._raza = raza #atributos privados
        self._f_nacimiento = f_nacimiento#atributos privados
        self._f_ingreso = f_ingreso#atributos privados

    def jugando(self):
        self.jugar = jugar

    def descripcion(self):
        print('Raza', self._raza, 'f_macimiento:', self._f_nacimiento, 'f_ingreso', self._f_ingreso)


class perro(animal):

    def __init__(self, nombre, direccion):
        super().__init__("salchicha", "23-02-2024", "21-04-2024")
        self._nombre = nombre
        self.direccion = direccion


class gato(animal):

    def __init__(self, nombre, direccion):
        super().__init__("salchicha", "23-02-2024", "21-04-2024")
        self.nombre = nombre
        self.direccion = direccion


miperro = perro("Atila", "san diego 336")
migato = gato("tokepi", "san diego 336")
miperro.descripcion()
#miperro.jugando()
print(f'Mi perro se llama {miperro._nombre}, es de raza {miperro._raza} y esta ')

#generar una clase animal--> 2 clases hijas perro y gato con los siguientes atributos
#padre--> raza, f_nacimiento, f_ingreso --- metodos : descripcion - accion (jugar)
#hijos--> nombre, direccion