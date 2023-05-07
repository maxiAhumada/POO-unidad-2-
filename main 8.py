from Clase import Conjunto

if __name__ == '__main__':
    lista=[0, 2, 4, 6, 5, 8, 10]
    A = Conjunto(lista)
    lista=[0, 4, 6, 9, 2, 5, 10]
    B = Conjunto(lista)
    A.mostrar ()
    B.mostrar ()
    while True:
        print ('opcion 1: union de dos conjuntos')
        print ('opcion 2: diferencia de dos conjuntos')
        print ('opcion 3: verificar si dos conjuntos son iguales')
        print ('opcion 4: salir')
        opcion = input ('ingresar opcion: \n')
        if opcion == '1':
            C = A + B
            C.mostrar ()
        elif opcion == '2':
            C = A - B
            C.mostrar ()
        elif opcion == '3':
            if A == B:
                print ('Los conjuntos A y B son iguales \n')
            else:
                print ('Los conjuntos A y B no son iguales \n')
        elif opcion == '4':
            break
        else:
            print ('opcion incorrecta')
