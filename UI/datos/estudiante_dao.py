from pyodbc import IntegrityError, ProgrammingError

from UI.datos.conexion import Conexion
from UI.dominio.estudiante import Estudiante


class EstuadianteDao:
    _INSERTAR = "INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo,estatura,peso,fecha_nacimiento) VALUES(?,?,?,?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = "select id,cedula,nombre,apellido,email,carrera,activo, estatura,peso,fecha_nacimiento from Estudiantes where cedula =?"

    _SELECCIONAR = "select id, cedula, nombre, apellido, email, carrera, activo, estatura ,peso ,fecha_nacimiento from Estudiantes where activo = 1"

    @classmethod
    def insertar_estudiante(cls, estudiante):
        # cursor = datos.conexion.Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mensaje': ''}
        Flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera,
                    estudiante.activo, estudiante.estatura, estudiante.peso, estudiante.fecha_nacimiento)
                cursor.execute(cls._INSERTAR, datos)
                Flag_exito = True
                mensaje = 'Ingreso exitoso'
        except IntegrityError as e:
            Flag_exito = False
            # print('la cedula que intenta ingresar ya existe')
            print(e)
            print(str(e))
            if e.__str__().find('Cedula') > 0:
                print('Cedula ya ingresada')
                mensaje = 'Cedula ya ingresada'
            elif e.__str__().find('Email') > 0:
                print('Email ya ingresada')
                mensaje = 'Email ya ingresada'
            else:
                print('Error de integridad')
                mensaje = 'Error de integridad'
        except ProgrammingError as e:
            Flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje = 'Los datos ingresados no son del tamaño permitido'
        except Exception as e:
            Flag_exito = False
            print(e)
        finally:
            respuesta['exito'] = Flag_exito
            respuesta['mensaje'] = mensaje
            # cursor.close()
            return respuesta

    @classmethod
    def seleccionar_por_cedula(cls, estudiante):
        persona_encontrada = None
        print(estudiante)
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.id = persona_encontrada[0]
                estudiante.cedula = persona_encontrada[1]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.email = persona_encontrada[4]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]

        except Exception as e:
            print(e)
        finally:
            return estudiante

    @classmethod
    def seleccionar_estudiantes(cls):
        lista_estudiantes = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._SELECCIONAR)
                for tupla_estudiante in resultado.fetchall():
                    estudiante = Estudiante()
                    estudiante.id = tupla_estudiante[0]
                    estudiante.cedula = tupla_estudiante[1]
                    estudiante.nombre = tupla_estudiante[2]
                    estudiante.apellido = tupla_estudiante[3]
                    estudiante.email = tupla_estudiante[4]
                    estudiante.carrera = tupla_estudiante[5]
                    estudiante.activo = tupla_estudiante[6]
                    estudiante.estatura = tupla_estudiante[7]
                    estudiante.peso = tupla_estudiante[8]
                    estudiante.dateEdit_fecha_nacimiento = tupla_estudiante[9]
                    lista_estudiantes.append(estudiante)
        except Exception as e:
            lista_estudiantes = None
        finally:
            return lista_estudiantes


if __name__ == '__main__':
    # e1 = Estudiante()
    # e1.cedula = '0996403317'
    # e1.nombre = 'Javier'
    # e1.apellido = 'Lindao'
    # e1.email = 'jlindao@gmail.com'
    # e1.carrera = 'Mark'
    # e1.activo = True
    # EstuadianteDao.insertar_estudiante(e1)
    # EstuadianteDao.seleccionar_por_cedula(e1)
    # print(e1)
    # persona_encontrada = EstuadianteDao.seleccionar_por_cedula(e1)
    # print(persona_encontrada)

    estudiantes = EstuadianteDao.seleccionar_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)
