class pantalones():

	def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def getMarca(self):
    	return self.marca

    def getPrecio(self):
    	return self.precio

class valores():

	lim5=0
	exis=0

	def __init__(self):
        self.lim5 = 0
        self.exis = 1

    def getlim5(self):
    	return self.lim5

    def getExis(self):
    	return self.exis

    def addLim5(self):
    	lim5=lim5+1

    def addExist(self):
    	exis=exis+1

    def subExist(self):
    	exis=exis-1

    def canSell(self):
    	return(lim5<5 and exis>1)


if __name__ == "__main__":  x=input()
    ropero.append(x)
    
    fl = input()
    n = 0
    x = 0
    temp = False

    for c in fl:
    	if( c == ' '):
    		temp = True
    	else:
    		if(temp):
    			x = x + c
    		else:
    			n = n + c


    ropero=[]
https://www.tutorialspoint.com/python/dictionary_get.htm

    x=input()
    ropero.append(x)

#tenemos el input ya funciona, solo un while n veces, esta todo en string hacer cast a entero
#cada while repetimos entrada de string del numero con esta tecnica
#metodo sacar
#