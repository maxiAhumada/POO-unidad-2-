from clases import Alumno
from clases import manejador_alumnos
from clases import Materia
from clases import manejador_materias
if __name__ == '__main__':
    mAlumnos = manejador_alumnos(9)
    mAlumnos.testalumnos()
    mMaterias = manejador_materias()
    mMaterias.testmaterias()
    while True:
        print('opcion 1: ingresar el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos')
        print('opcion 2: ingresar el nombre de una materia, e informar los estudiantes que la aprobaron en forma promocional, con nota mayor o igual que 7.')
        print('opcion 3: Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre')
        print('opcion 4: salir')
        opcion = input('ingresar opcion: \n')
        if opcion == '1':
            dni = input ('ingresar numero de dni: \n')
            mMaterias.buscardni(dni)
        if opcion == '2':
            materia = input ('ingresar nombre de la materia: \n')
            lista_dni = mMaterias.buscarmateria(materia)
            print(lista_dni)
            print("DNI      Apellido y nombre       Fecha       Nota        Año que cursa \n")
            for dni in lista_dni:
                mAlumnos.buscarpordni(dni)
        if opcion == '3':
            mAlumnos.ordenar()
        if opcion == '4':
            break
        else: 
            print('opcion incorrecta')


