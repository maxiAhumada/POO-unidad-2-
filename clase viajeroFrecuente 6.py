class viajero:
    __numero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = ''
    def __init__(self,num,dni,nomb,ape,millas):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas = millas
    def __str__ (self):
        return '%s %s %s %s %s' % (self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas)
    
    def __gt__ (self,otro):
        return self.millas > otro.millas
    def busqueda (self,numero):
        elem = None
        i = 0
        while i < len(viajero) and not elem:
            if viajero[i].__numero == numero:
                elem = viajero[i]
            else:
                i =+ 1
        return elem
    def __add__(self, millas):
        return viajero(self.numero, self.nombre, self.millas + millas)
    def __sub__(self,millas):
        return viajero(self.numero, self.nombre, self.millas - millas)

if __name__ == '__main__':
    viajeros = []
    with open('viajeros.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            instancia = viajero(datos[0],datos[1],datos[2],datos[3],int(datos[4]))
            viajeros.append(instancia)
    for viajerofrecuente in viajeros:
        viajerofrecuente.mostrarviajero()
    max_millas = 0
    viajeros_max_millas = []
        
    for viajero in viajeros:
        if viajero > max_millas:
            max_millas = viajero.get_millas()
            viajeros_max_millas = [viajero]
        elif viajero == max_millas:
            viajeros_max_millas.append(viajero)
    print(f'viajeros con mayor cantidad de millas {viajeros_max_millas}')
    codigo = input ('numero viajero frecuente:')
    encontrado = viajero ('','','','','')
    encontrado = viajeros.busqueda(codigo)
    if encontrado:
        num = input ('ingrese millas a acumular: \n')
        encontrado += num
        num = input ('ingrese millas a canjear: \n')
        encontrado -= num
