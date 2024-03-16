import sympy as sp
import math 

x = sp.Symbol('x')
class NumericIntegration : 
    def __init__(self, a, b, f, M):
        self.a = a
        self.b = b
        self.f = f
        self.M = M
        
    def getTrap(self):
        h = (self.b - self.a)/self.M
        s = 0
        fun = sp.lambdify(x, self.f)
        for k in range(1, self.M):
            val = self.a + h*k
            s += fun(val)
        return h*(fun(self.a) + fun(self.b))/2 + h*s
    
    def getSimp(self):
        h = (self.b - self.a)/self.M
        s = 0
        fun = sp.lambdify(x, self.f)
        for k in range(1, self.M+1):
            xi = self.a + h*(k - 1)
            xi1 = xi + h
            s += fun(xi)+4*fun((xi + xi1)/2)+fun(xi1)
        return h*s/6

while True:
    option = input("elija una opcion: \n 1) Aproximar integral con metodo de trapecios \n 2) Aproximar integral con metodo de simpson \n 3) Salir  \n :   ")
    if option == "1":
        a = float(eval(input("ingrese el extremo izquierdo de la integral a evaluar (usar la libreria math si requiere): ")))
        b = float(eval(input("ingrese el extremo derecho de la integral a evaluar (usar la libreria math si requiere): ")))
        f = eval(input("Ingrese la funcion  usando sympy, ejemplo: ' sp.cos(x) + 1/x': "))
        m = int(input("ingrese el numero de particiones del intervalo: "))
        intgr = NumericIntegration(a, b, f, m)
        print(intgr.getTrap())
    if option == "2":
        a = float(eval(input("ingrese el extremo izquierdo de la integral a evaluar (usar la libreria math si requiere): ")))
        b = float(eval(input("ingrese el extremo derecho de la integral a evaluar (usar la libreria math si requiere): ")))
        f = eval(input("Ingrese la funcion  usando sympy, ejemplo: ' sp.cos(x) + 1/x': "))
        m = int(input("ingrese el numero de particiones del intervalo: "))
        intgr = NumericIntegration(a, b, f, m)
        print(intgr.getSimp())
    if option == "3":
        print("gracias por usar el programa :)")
        break

        
