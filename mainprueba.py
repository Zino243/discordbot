from matrizcsv import matrizdebusqueda as mtbq
from buscadorcsv import finder as fd

x = 5
y = 6

t = mtbq.busqueda(x, y)
n = fd.name(x, y)
print(t)

if t:
    print("las coordenadas estan elegidas por {}".format(n))
else:
    print("puedes contruir aqui")
