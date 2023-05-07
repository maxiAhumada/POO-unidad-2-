from clase_registro import registro
if __name__ == '__main__':
    lista = []
    for i in range(30):
        lista.append([])
        for j in range(24):
            lista[i].append(None)

    with open("datos_atm.txt") as archivo:
        for linea in archivo:
            data = linea.strip().split(",")
            inst = registro(data[2], data[3], data[4])
            i = int(data[0]) - 1
            j = int(data[1])
            lista[i][j] = inst
    while True:
         print("Selecciona una opción:")
         print("1. Mostrar para cada variable el día y hora de menor y mayor valor ")
         print("2. Indicar la temperatura promedio mensual por cada hora")
         print("3. listar los valores de las tres variables para cada hora del día dado")
         print("4. Salir")
         opcion = input ('ingrese la opcion')
         if opcion == '1':
            lista.calculo_max(lista)
            lista.calculo_min(lista)
         elif opcion == '2':
            lista.promedio(lista)
         elif opcion == '3':
            num = input ('ingrese dia a mostrar')
            lista.listar(lista,num)
         elif opcion == '4':
            break
         else:
            print ('opcion no valida')

             


    

