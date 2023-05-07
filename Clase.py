class Conjunto:
    __numeros = []
    def __init__(self, lista):
        self.__numeros = lista
    def __add__ (self, otro):
        nueva_lista = self.__numeros.copy()
        for elemento in otro.__numeros:
            if elemento not in nueva_lista:
                nueva_lista.append(elemento)
        return Conjunto(nueva_lista)
    def mostrar (self):
        print (self.__numeros)
    def __sub__ (self,otro):
        nuevos_numeros = [num for num in self.__numeros if num not in otro.__numeros]
        return Conjunto(nuevos_numeros)
    def __eq__ (self,otro):
        for e in self.__numeros:
            if e not in otro.__numeros:
                return False
        return True 
            