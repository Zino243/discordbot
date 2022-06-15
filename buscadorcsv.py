import pandas as pd

data = pd.read_csv('supermarket.csv', header=0)

class finder():
    def finderx(self, valx):
        cx = data['CoordX']
        try:
            cx = int(cx[cx==valx])
            try:
                if cx == valx:
                    result = True
                    return result
            except:
                result = False
                return result
        except:
            cx = False

    def findery(self, valy):
        cy = data['CoordY']
        try:
            cy = int(cy[cy==valy])
            try:
                if cy == valy:
                    result = True
                    return result
            except:
                result = False
                return result
        except:
            cy = False

    def name(x, y):
        dtx = data[data.CoordX == x]["Nombre"]
        dty = data[data.CoordY == y]["Nombre"]
        dtx = str(dtx.item())
        dty = str(dty.item())

        #print("{} --- {}".format(dtx.item(),dty.item()))
        if dtx == dty:
            return dtx





#f = finder()
#f = f.name(5,6)
#print(type(f))


#print(dt.item())
#if dt.item() == 'a':
#    print("correct")



#data = data[data["CoordX"]== x]["Nombre"]


#finder = finder()
#if finder.finderx(int(input('-> '))):
#    print("resultado correcto")
#else:
#    print("Error")
