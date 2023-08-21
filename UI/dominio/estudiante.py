#yuletsy fong
#gregorio rosales

from UI.dominio.persona import Persona
from datetime import datetime

#from dominio.persona import Persona
class Estudiante(Persona):
    contador_estudiante = 0
    contador_id = 0

    def __init__(self, cedula: str=None, nombre: str=None, apellido: str=None, email: str=None, telefono: str=None, direccion: str=None,
                 numero_libros: int=0, activo: bool=True, carrera: str=None, nivel: int=1, estatura= int, peso=float, fecha_nacimiento =datetime, edad=None):

        Estudiante.contador_estudiante += 1
        Estudiante.contador_id += 1
        self._id = Estudiante.contador_estudiante
        self._nivel = nivel
        super(Estudiante, self).__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email,
                                         telefono=telefono, direccion=direccion, numero_libros=numero_libros,
                                         activo=activo, carrera=carrera, estatura=estatura, peso=peso, fecha_nacimiento=fecha_nacimiento,edad=edad)

    def __str__(self):
        return f' Estudiante : {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
    e1 = Estudiante(cedula='0950643973', nombre='gregorio', apellido='rosales', email='gregoriorosales42@gmail.com',
                    telefono='0961228092', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e2 = Estudiante(cedula='0951249390', nombre='yuletsy', apellido='fong', email='yulyfong@gmail.com',
                    telefono='0995182475', direccion='pascuales', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e3 = Estudiante(cedula='0952822294', nombre='Leandro', apellido='Urbina', email='leandrour@gmail.com',
                    telefono='0986179963', direccion='Trinitaria', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
    e4 = Estudiante(cedula='0989547152', nombre='Luis', apellido='Llerena', email='luisllerena@gmail.com',
                    telefono='0993062825', direccion='Suburbio', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)

    print(e1)
    print(e2)
    print(e3)
    print(e4)