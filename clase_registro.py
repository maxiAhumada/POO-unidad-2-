class registro:
    __temp = ''
    __hmd = ''
    __presion = ''
    def __init__(self,temp,hmd,presion):
        self.__temp = temp
        self.__hmd = hmd
        self.__presion = presion

    def calculo_max (self,lista):
        max_temp = 0
        d_temp = 0
        h_temp =0
        max_hmd = 0
        d_hmd = 0
        h_hmd =0
        max_pres = 0
        d_pres = 0
        h_pres =0
        for dia in lista:
            for hora in dia:
                temp,hmd,pres = hora
                if temp > max_temp:
                    max_temp = temp
                    d_temp = dia
                    h_temp = hora
                if hmd > max_hmd:
                    max_hmd = hmd
                    d_hmd = dia
                    h_hmd = hora
                if pres > max_pres:
                    max_pres = pres
                    d_pres = pres
                    h_pres = pres
        
        print (f'maxima temperatura: dia {d_temp}, hora {h_temp}, valor {max_temp}')        
        print (f'maxima humedad: dia {d_hmd}, hora {h_hmd}, valor {max_hmd}')    
        print (f'maxima presion: dia {d_pres}, hora {h_pres}, valor {max_pres}')  
    def calculo_min (self,lista):
        min_temp = 9999
        d_temp = 0
        h_temp =0
        min_hmd = 9999
        d_hmd = 0
        h_hmd =0
        min_pres = 9999
        d_pres = 0
        h_pres =0
        for dia in lista:
            for hora in dia:
                temp,hmd,pres = hora
                if temp < min_temp:
                    min_temp = temp
                    d_temp = dia
                    h_temp = hora
                if hmd > min_hmd:
                    min_hmd = hmd
                    d_hmd = dia
                    h_hmd = hora
                if pres > min_pres:
                    min_pres = pres
                    d_pres = pres
                    h_pres = pres
        
        print (f'minima temperatura: dia {d_temp}, hora {h_temp}, valor {min_temp}')        
        print (f'minima humedad: dia {d_hmd}, hora {h_hmd}, valor {min_hmd}')    
        print (f'minima presion: dia {d_pres}, hora {h_pres}, valor {min_pres}')  
    def promedio (self,lista):
        temp_total = 0
        for dia in lista:
            for hora in dia:
                temp = hora
                temp_total += temp
        prom = temp_total/len(dia)
        print (f'promedio mensual de temperatura {prom}')
    def listar (self,lista,num):
        print ('Hora    Temperatura    Humedad     Presion \n')
        for hora, registro in enumerate(lista[num-1]):
            print (f'{hora+1}   {registro.temp}    {registro.hmd}   {registro.pres} \n')
            




                

        



