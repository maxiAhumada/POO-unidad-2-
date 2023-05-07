class Ventana:
    __titulo = ''
    __valorx_viz = ''
    __valory_viz = ''
    __valorx_vdr = ''
    __valory_vdr = ''
    def __init__(self,titulo,x_viz=0,y_viz=0,x_vdr=500,y_vdr=500):
        self.__titulo = titulo
        self.__valorx_viz = x_viz
        self.__valory_viz = y_viz
        self.__valorx_vdr = x_vdr
        self.__valory_vdr = y_vdr
    def mostrar (self):
        print (f'titulo ventana: {self.__titulo}')
        print (f'valores vertices x,y vertice superior izquierdo {self.__valorx_viz},{self.__valory_viz}')
        print (f'valores vertices x,y vertice inferior derecho {self.__valorx_vdr},{self.__valory_vdr}')
    def getTitulo (self):
        return self.__titulo
    def alto (self):
        altura = self.__valory_viz - self.__valory_vdr
        return altura
    def ancho (self):
        largo = self.__valorx_viz - self.__valorx_vdr
        return largo
    def moverDerecha (self,unidad=1):
        nviz = self.__valorx_viz + unidad
        nvdr = self.__valorx_vdr + unidad
        if nviz < nvdr:
            self.__valorx_viz += unidad
            if nvdr <= 500:
                self.__valorx_vdr += unidad
            else: print('no es posible el desplazamiento')
        else: print('no es posible el desplazamiento')
    def moverIzquierda (self,unidad=1):
        nviz = self.__valorx_viz - unidad
        nvdr = self.__valorx_vdr - unidad
        if nvdr > nviz:
            self.__valorx_vdr-= unidad
            if nviz >= 0:
                self.__valorx_viz -= unidad
            else: print('no es posible el desplazamiento')
        else: print('no es posible el desplazamiento')
    def bajar (self,unidad=1):
        nviz = self.__valory_viz - unidad
        nvdr = self.__valory_vdr - unidad
        if nvdr > nviz:
            self.__valory_vdr -= unidad
            if nviz >= 0:
                self.__valory_viz -= unidad
            else: print('no es posible el desplazamiento')
        else: print('no es posible el desplazamiento')       
    def subir (self,unidad=1):
        nviz = self.__valory_viz + unidad
        nvdr = self.__valory_vdr + unidad
        if nviz < nvdr:
            self.__valory_viz += unidad
            if nvdr <= 500:
                self.__valory_vdr += unidad
            else: print('no es posible el desplazamiento')
        else: print('no es posible el desplazamiento')

    