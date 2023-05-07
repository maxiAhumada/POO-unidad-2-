import numpy as np
import csv

class Alumno:
    def __init__ (self,dni,apelliido,nombre,carrera,año_carrera):
        self.__dni = dni
        self.__apellido = apelliido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año_carrera
    def __str__ (self):
        return "%s      %s      %s      %s      %s \n" % (self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__año)
    def __lt__ (self,otro):
        if self.__año != otro.getaño():
            return self.__año < otro.getaño()
        else:
            return (self.__apellido.lower(),self.__nombre.lower()) < (otro.getapellido().lower(),otro.getnombre().lower())
    def getdni (self): 
        return self.__dni
    def getapellido (self):
        return self.__apellido
    def getnombre (self):
        return self.__nombre
    def getcarrera (self):
        return self.__carrera
    def getaño (self):
        return self.__año
                 
class manejador_alumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__ (self,dimension,incremento=5):
        self.__alumnos = np.empty(dimension,dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregaralumno (self,alumno):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad] = alumno
        self.__cantidad += 1
    def getalumno (self,indice):
        return self.__alumnos[indice]
    def testalumnos (self):
        with open ('alumnos.csv') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                alumno = Alumno(datos[0],datos[1],datos[2],datos[3],datos[4])
                self.agregaralumno(alumno)
    def buscarpordni (self,dni):
        for alumno in self.__alumnos:
            if alumno.getdni() == dni:
              print(alumno) 
    def ordenar (self):
        ordenados = sorted(self.__alumnos)
        for alumno in ordenados:
            print (alumno)

class Materia:
    def __init__ (self,dni,nombre,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    def __str__ (self):
        return '%s %s %s %s %s' % (self.__dni,self.__nombre,self.__fecha,self.__nota,self.__aprobacion)
    def getdni (self):
        return self.__dni
    def getnombre (self):
        return self.__nombre
    def getfecha (self):
        return self.__fecha
    def getnota (self):
        return self.__nota
    def getaprobacion (self):
        return self.__aprobacion
    
class manejador_materias:
    def __init__ (self):
        self.__lista_materias = []
    def agregarmateria (self,materia):
        self.__lista_materias.append(materia)
    def testmaterias (self):
        with open('materiasAprobadas.csv') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                materia = Materia(datos[0],datos[1],datos[2],datos[3],datos[4])
                self.agregarmateria(materia)
    def buscardni (self,dni):
       cont_aplazos = 0
       acum_aplazos = 0
       cont_sinap = 0
       acum_sinap = 0
       nota = 0
       for materia in self.__lista_materias:
           if dni == materia.getdni():
                cont_aplazos += 1
                nota = materia.getnota()
                acum_aplazos += int(nota)
                if materia.getaprobacion() != 'E':
                    cont_sinap += 1
                    acum_sinap += int(nota)
       promedio_con = acum_aplazos / cont_aplazos
       promedio_sin = acum_sinap / cont_sinap
       print('pormedio del alumno con dni {}: con aplazos: {} sin aplazos {}'.format(dni,np.round(promedio_con,2),np.round(promedio_sin,2)))
    def buscarmateria(self, nombre_materia):
        dni_promocionales = []  
        for materia in self.__lista_materias:
            if materia.getnombre() == nombre_materia:  
                if materia.getaprobacion() == 'P':
                    if int(materia.getnota()) >= 7:
                        agregar = materia.getdni()
                        dni_promocionales.append(agregar)
        return dni_promocionales

                    
                    





