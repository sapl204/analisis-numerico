import math
import sympy as sp
from tabulate import tabulate

x = sp.Symbol('x')

class Hermite:
    def __init__(self, xpoints, ypoints, ypPoints, p0 ,f):
        self.xpoints = xpoints
        self.ypoints = ypoints
        self.ypPoints = ypPoints
        self.p0 = p0
        self.f = f

    def __getLnk(self, points, j):
        prod = 1
        for k in range(0, len(points)):
            if j == k:
                continue
            else:
                prod *= (x - points[k])/(points[j] - points[k])
        return prod

    def __showPol(self, tableData, heads, pol ):
        polSim = sp.simplify(pol)
        print(f"polinomio interpolante de hermite completo : {pol}")
        tableData.append([polSim, sp.lambdify(x, polSim)(self.p0)])
        print(tabulate(tableData, headers = heads, tablefmt = "grid"))
        sp.plot(polSim, title = "polinomio interpolante de Hermite")

    @property
    def getHermiteByPoints(self):
        heads = ["H(x)", f"H({self.p0})"]
        tableData = []
        pol = 0
        for j in range(0, len(self.xpoints)):
            prod = self.__getLnk(self.xpoints, j)
            dvProd = sp.diff(prod, x)
            dvProdInXj = sp.lambdify(x, dvProd)(self.xpoints[j])
            pol += self.ypoints[j]*(1-2*(x - self.xpoints[j])*dvProdInXj)*prod**2 + self.ypPoints[j]*(x - self.xpoints[j])*prod**2
        self.__showPol(tableData, heads, pol)
    
    @property
    def getHermiteByFunction(self):
        heads = ["H(x)", f"H({self.p0})"]
        tableData = []
        pol = 0
        dvF = sp.diff(self.f, x)
        for j in range(0, len(self.xpoints)):
            prod = self.__getLnk(self.xpoints, j)
            dvProd = sp.diff(prod, x)
            dvProdInXj = sp.lambdify(x, dvProd)(self.xpoints[j])
            dvFInXj = sp.lambdify(x, dvF)(self.xpoints[j])
            fInXj = sp.lambdify(x, self.f)(self.xpoints[j])       
            pol += fInXj*(1-2*(x - self.xpoints[j])*dvProdInXj)*prod**2 + dvFInXj*(x - self.xpoints[j])*prod**2
        self.__showPol(tableData, heads, pol)
                
def kpointsToArray(kpointsStr):
    kpointSplited = kpointsStr.split(",")
    kpoints = list(map(lambda x : float(x), kpointSplited ))
    return kpoints

while True:
    option = input("elija una opcion: \n 1) Calcular el polinomio interpolante de Hermite con puntos \n 2) Calcular el polinomio interpolante de Hermite con la funcion \n 3) Salir  \n :   ")
    if option == "1":
        p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
        xpointStr = input("ingrese los puntos de x separados por , : ")
        ypointStr = input("ingrese los puntos y separados por , : ")
        ypPointStr = input("ingrese los puntos y' separados por , :")
        her = Hermite(kpointsToArray(xpointStr), kpointsToArray(ypointStr), kpointsToArray(ypPointStr), p0, None)
        her.getHermiteByPoints

    if option == "2":
        p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
        xpointStr = input("ingrese los puntos de x separados por , : ")
        f = eval(input("Ingrese la funcion  usando sympy, ejemplo: ' sp.cos(x) + 1/x': "))
        her = Hermite(kpointsToArray(xpointStr), [], [], p0, f)
        her.getHermiteByFunction
    if option == "3":
        print("gracias por usar el programa :)")
        break
