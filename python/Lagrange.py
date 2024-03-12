import math
from tabulate import tabulate
import sympy as sp
x = sp.Symbol('x')
class Lagrange:
    def __init__(self, xpoints, ypoints,p0, f):
        self.xpoints = xpoints
        self.ypoints = ypoints
        self.p0 = p0
        self.f = f

    def __getLnk(self, points, k):
        prod = 1
        for j in range(0, len(points)):
            if j == k:
                continue
            else:
                prod *= (x - points[j])/(points[k] - points[j])
        return prod
 
    def __showPol(self, tableData, heads, pol):
        polSim = sp.simplify(pol)
        print(f"polinomio interpolante de Lagrange completo {pol}")
        tableData.append([polSim, sp.lambdify(x, polSim)(self.p0)])
        print(tabulate(tableData, headers = heads, tablefmt = "grid"))
        sp.plot(pol, title = "polinomio interpolante de Lagrange")

    def getLagrByFunction(self):
        heads = ["p(x)", f"p({self.p0})"]
        tableData = []
        fun = sp.lambdify(x, self.f)
        pol = 0
        for k in range(0, len(self.xpoints)):
            prod = self.__getLnk(self.xpoints, k)
            pol += fun(self.xpoints[k])*prod
        self.__showPol(tableData, heads, pol)

    def getLagrByPoints(self):
        heads = ["p(x)", f"p({self.p0})"]
        tableData = []
        pol = 0
        for k in range(0, len(self.xpoints)):
            prod = self.__getLnk(self.xpoints, k)
            pol += self.ypoints[k]*prod
        self.__showPol(tableData, heads, pol)

def kpointsToArray(kpointsStr):
    kpointSplited = kpointsStr.split(",")
    kpoints = list(map(lambda x : float(x), kpointSplited ))
    return kpoints

while True:        
    option = input("elija una opcion: \n 1) Calcular el polinomio interpolante de Lagrange con puntos \n 2) Calcular el polinomio interpolante de Lagrange con la funcion \n 3) Salir  \n :   ")
    if option == "1":
        p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
        xpointStr = input("ingrese los puntos de x separados por , : ")
        ypointStr = input("ingrese los puntos y separados por , : ")
        lagr = Lagrange(kpointsToArray(xpointStr), kpointsToArray(ypointStr), p0, None)
        lagr.getLagrByPoints()
    if option == "2":
        p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
        xpointStr = input("ingrese los puntos de x separados por , : ")
        f = eval(input("Ingrese la funcion  usando sympy, ejemplo: ' sp.cos(x) + 1/x': "))
        lagr = Lagrange(kpointsToArray(xpointStr), None, p0, f)
        lagr.getLagrByFunction()
    if option == "3":
        print("gracias por usar el programa :)")
        break
