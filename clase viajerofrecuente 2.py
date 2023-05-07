class viajero:
    __numero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasac = 0
    def __init__(self,num,dni,nomb,ape,millac):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nomb
        self.__apellido = ape
        self.__millasac = millac
    
    def totalmillas (self):
        return self.__millasac
    
    def acumularm (self,acum):
        nvmillas = self.__millasac + int(acum)
        return nvmillas
   
    def canjearm (self,canje):
        if canje > self.__millasac:
            print ("no posee esa cantidad de millas")
        else:
            self.__millasac -= canje
            print ('nueva cantidad de millas acumuladas {self.__millasac}')
        return self.__millasac
    def mostrarviajero (self):
            print (self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millasac)
    def busqueda (self,numero):
        elem = None
        i = 0
        while i < len(viajero) and not elem:
            if viajero[i].__numero == numero:
                elem = viajero[i]
            else:
                i =+ 1
        return elem
if __name__ == '__main__':
    viajeros = []
    with open('viajeros.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            instancia = viajero(datos[0],datos[1],datos[2],datos[3],int(datos[4]))
            viajeros.append(instancia)
    for viajerofrecuente in viajeros:
        viajerofrecuente.mostrarviajero()
    num = input ('numero viajero frecuente:')
    encontrado = viajero ('','','','','')
    encontrado = viajeros.busqueda(num)
    if encontrado:
        while True:
            print("Selecciona una opción:")
            print("1. Consultar Cantidad de Millas")
            print("2. Acumular Millas")
            print("3. Canjear Millas")
            print("4. Salir")
            opcion = input ('ingrese la opcion')

            if opcion == "1":
                print ('cantidad total de millas {}'.encontrado.totalmillas())
            elif opcion == "2":
                acum = input('ingrese cantidad de millas a acumular')
                encontrado.acumularm(acum)
            elif opcion == "3":
                cant = input('ingrese cantidad de millas a canjear')
                nvmillas = encontrado.canjearm
            elif opcion == "4":
                break
            else:
                print ('opcion no valida')
    else:
        print ('no se encontro un viajero con el numero {num}')            
