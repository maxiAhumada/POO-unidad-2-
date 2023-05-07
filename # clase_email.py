
class email:
    __ID = ''
    __dom = ''
    __tipo = ''
    __pas = ''
    def __init__ (self,ID,dom,tipo,pas):
        self.__ID = ID
        self.__dom = dom
        self.__tipo= tipo
        self.__pas = pas
    def retornaemail (self,ID,dom,tipo):
        return self.__ID + '@' + self.__dom + '.' + self._tipo 
    def getdominio (self):
        return self._sueldo
    def crearcuenta (self,correo):
        self.__ID,self._Dom = correo.split("@")
        self.__dom,self.__tipo = correo.split(".")
    def ver_cont (self,cont):
        if self._pas == cont:
            ret = 1
        else:
            ret = 2
        return ret
    def cambio_cont (self,nuevo):
        self.__pas = nuevo 
    def valid (self,correo):
        if '' in correo:
            ret = 1
        else:
            ret = 2
        return ret
if __name__ == '__main__':
    nomb = input('nombre:')
    nvcorreo = email(input('ID de la cuenta:'),
            input('dominio:'),
            input('tipo de dominio:'),
            input('contraseña:'))
    print (nomb)
    nvcorreo.retornaemail ()
    pas = input ('ingrese contraseña:')
    band = pas.ver_cont
    if band == 1:
        nvpas = input ('ingese nueva contraseña')
        nvpas.cambio_cont
    nvemail = input ('ingrese direccion de correo')
    nvemail = email ('','','','')
    nvemail.crearcuenta
    lis = []
    with open("","") as archivo:
        for fila in archivo:
            nv = fila.split(',')
            if nv[0] != '':
                if nv[1] != '':
                   if nv[2] != '':
                       print ('correo valido')
                   else: 
                       print ('correo no valido')
                else: 
                    print ('correo no valido')
            else: 
                print ('correo no valido')
            list[fila] = email 
            
        


    
    




