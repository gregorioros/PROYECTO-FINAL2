# luis llerena
# yuletsy fong
# leandro urbina
# gregorio rosales

from estudiante import Estudiante
from libro import Libro


class Pedido():
    contador_pedido = 0

    def __init__(self, solicitante, lista_materiales, fecha_prestamo, fecha_devolucion):
        Pedido.contador_pedido += 1
        self._id = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_materiales = lista_materiales
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f'Pedido: {self.__dict__}'

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, nuevo_id):
    #     self._id = nuevo_id

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, nuevo_solicitante):
        self._solicitante = nuevo_solicitante

    @property
    def lista_materiales(self):
        return self._lista_materiales

    @lista_materiales.setter
    def lista_materiales(self, nueva_lista_materiales):
        self._lista_materiales = nueva_lista_materiales

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nueva_fecha_prestamo):
        self._fecha_prestamo = nueva_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha_devolucion):
        self._fecha_devolucion = nueva_fecha_devolucion

    def mostrar_solicitante(self):
        print('Solicitante:')
        print(f'\tNombre: {self.solicitante.nombre.upper()}')
        print(f'\tApellido: {self.solicitante.apellido.upper()}')
        print(f'\tCedula: {self.solicitante.cedula}')
        if isinstance(self.solicitante, Estudiante):
            print(f'\tTipo: Estudiante')
        else:
            print(f'\tTipo: Docente')

    def mostrar_materiales(self):
        print('Listado Materiales'.center(50, '*'))
        print(f'Cantidad de Mateiriales Pedidos: {len(self.lista_materiales)}')
        for material in self.lista_materiales:
            if isinstance(material, Libro):
                print('Libro'.center(50, '*'))
            else:
                print('Revista'.center(50, '*'))
            print(f'\tTitulo: {material.titulo}')
            print(f'\tAutor: {material.autor}')
            print(f'\tCantidad Disponible: {material.cantidad_disponible}')

    def mostrar_pedido(self):
        print('Solicitante:')
        print(f'\tNombre: {self.solicitante.nombre.upper()}')
        print(f'\tApellido: {self.solicitante.apellido.upper()}')
        print(f'\tCedula: {self.solicitante.cedula}')
        if isinstance(self.solicitante, Estudiante):
            print(f'\tTipo: Estudiante')
        else:
            print(f'\tTipo: Docente')
        print('Listado Materiales'.center(50, '*'))
        print(f'Cantidad de Mateiriales Pedidos: {len(self.lista_materiales)}')
        for material in self.lista_materiales:
            if isinstance(material, Libro):
                print('Libro'.center(50, '*'))
            else:
                print('Revista'.center(50, '*'))
            print(f'\tTitulo: {material.titulo}')
            print(f'\tAutor: {material.autor}')
            print(f'\tCantidad Disponible: {material.cantidad_disponible}')


if __name__ == '__main__':
    pass
