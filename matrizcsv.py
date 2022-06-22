from unittest import result
from buscadorcsv import finder as fd
finder = fd()

def rangerX(xneg, xpos):
    for i in range(xneg, xpos):
        if finder.finderx(i + 1):
            return True

def rangerY(yneg, ypos):
    for j in range(yneg, ypos):
        if finder.findery(j + 1):
            return True

class matrizdebusqueda():
    def busqueda(x: int, y: int):
        #el 50 es el rango que creas para buscar dentro de todos lo numeros dentro del cuadrado, es decir desde x-50 hasta x+50 y desde y-50 hasta y+50 haciendo el cuadrado
        xpos = x + 5
        xneg = x - 5
        ypos = y + 5
        yneg = y - 5

        resultX = rangerX(xneg, xpos)
        resultY = rangerY(yneg, ypos)
        
        print("x --- {}".format(resultX))
        print("y --- {}".format(resultY))
        if resultX and resultY:
            return True



#busca = matrizdebusqueda()
#Aqui le metes la coord X y la coord Y consecutivamente
#print(busca.busqueda(21, 2))
