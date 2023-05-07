import csv 
class PlanAhorro:
    cuotasplan = 60
    cuotaslicitar = 10
    def __init__(self,codigo,modelo,version,valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
    def __str__(self):
        return "%s %s %s %s" % (self.__codigo,self.__modelo,self.__version,self.__valor)
    def getcodigo (self):
        return self.__codigo 
    def getmodelo (self):
        return self.__modelo
    def getversion (self):
        return self.__version
    def getvalor (self):
        return self.__valor 
    @classmethod
    def getcuotasplan (cls):
        return cls.cuotasplan
    @classmethod
    def getcuotaslicitar (cls):
        return cls.cuotaslicitar
    def actualizar_valor (self,nuevo):
        self.__valor = nuevo
    def actualizar_cuotas_licitar (self,nv):
        self.__class__.cuotaslicitar = nv
class manejador_plan:
    def __init__ (self):
        self.__listaplanes = []
    def agregarplan (self,coche):
        self.__listaplanes.append(coche)
    def testplanes (self):
        with open("planes.csv") as archivo:
            for line in archivo:
                datos = line.strip().split(";")
                inst = PlanAhorro(datos[0],datos[1],datos[2],int(datos[3]))
                self.agregarplan(inst)
        archivo.close()
    def actualizar_valores(self):
        for plan in self.__listaplanes:
            print(f"Plan: {plan._PlanAhorro__codigo} - Modelo: {plan._PlanAhorro__modelo} - Version: {plan._PlanAhorro__version}")
            nuevo_valor = float(input("Ingrese el nuevo valor del vehiculo: "))
            plan.actualizar_valor(nuevo_valor)
    def buscarporvalor (self,valor):
        for plan in self.__listaplanes:
            valorcuota = (plan.getvalor() / plan.getcuotasplan()) + plan.getvalor() * 0.10
            if valorcuota < int(valor):
                print(f"codigo: {plan._PlanAhorro__codigo} - Modelo: {plan._PlanAhorro__modelo} - Version: {plan._PlanAhorro__version}") 
    def montolicitar (self):
        for plan in self.__listaplanes:
            valorcuota = (plan.getvalor() / plan.getcuotasplan()) + plan.getvalor() * 0.10
            valorlicitar = plan.getcuotaslicitar() * valorcuota
            print(f'para el vehiculo: codigo: {plan._PlanAhorro__codigo} - Modelo: {plan._PlanAhorro__modelo} - Version: {plan._PlanAhorro__version} /n')
            print(f'valor licitacion {int(valorlicitar)}')
    def buscarcodigo (self,cod):
        resultado = filter(lambda x: x.getcodigo() == codigo, self.__listaplanes)
        return next(resultado, None)
    
if __name__ == '__main__':
    mp = manejador_plan()
    mp.testplanes()
while True:
    print ('opcion 1: actualizar valor del vehiculo de cada plan')
    print ('opcion 2: Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado')
    print ('opcion 3: Mostrar el monto que se debe haber pagado para licitar el vehículo')
    print ('opcion 4: Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar')
    print ('opcion 5: salir')
    opcion = input ('ingresar opcion:')
    if opcion == '1':
        mp.actualizar_valores()
    elif opcion == '2':
        valor = input ('ingresar valor a buscar')
        mp.buscarporvalor (valor)
    elif opcion == '3':
        mp.montolicitar()
    elif opcion == '4':
        codigo = input ('ingresar codigo a buscar')
        cambiar = mp.buscarcodigo(codigo)
        if cambiar:
            nvcuotas = input ('ingresar nueva cantidad de cuotas para licitar')
            cambiar.actualizar_cuotas_licitar(nvcuotas)
            print(f"Las cuotas necesarias para licitar del plan {codigo} han sido actualizadas a {nvcuotas}.")
        else:
            print(f"No se ha encontrado un plan con el código {codigo}.")
        
    elif opcion == '5':
        break
    else: print('opcion incorrecta')



        

    
