import math
from tabulate import tabulate
import sympy as sp

x = sp.Symbol('x')
def polinomio(points, f, p0):
    heads = ["p(x)", "p("+str(p0)+")"]
    tableData = []
    fun = sp.lambdify(x, f)
    polinomio = 0
    for k in range(0, len(points)):
        prod = 1
        for i in range(0, len(points)):
            if i == k:
                continue
            else:
                prod *= (x - points[i] )/(points[k] - points[i])
        polinomio += fun(points[k])*prod
    polinomioInter = sp.lambdify(x, polinomio)
    tableData.append([polinomio, polinomioInter(p0)])
    print(tabulate(tableData, headers = heads, tablefmt = "grid"))


p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
f = eval(input("Ingrese la funcion  usando sympy, ejemplo: 'sp.cos(x) + 1/x': "))
pointsStr = input("ingrese los puntos que quiere ingresar separados por , : ")
pointsArr = pointsStr.split(",")
points = list(map(lambda x: float(x), pointsArr))
print(polinomio(points, f, p0))
