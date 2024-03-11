import math
import sympy as sp
from tabulate import tabulate

x = sp.Symbol('x')
def polHermite(xpoints, ypoints, ypPoints, p0):
    heads = ["H(x)", f"H({p0})"]
    tableData = []
    pol = 0
    for j in range(0, len(xpoints)):
        prod = 1
        for k in range(0, len(xpoints)):
            if j == k:
                continue
            else:
                prod *= (x - xpoints[k])/(xpoints[j] - xpoints[k])
        dvProd = sp.diff(prod, x)
        dvProdInXj = (sp.lambdify(x, dvProd))(xpoints[j])
        pol += ypoints[j]*(1-2*(x - xpoints[j])*dvProdInXj)*prod**2 + ypPoints[j]*(x - xpoints[j])*prod**2        
    
    polSim = sp.simplify(pol)
    tableData.append([polSim, sp.lambdify(x, polSim)(p0)])
    print(tabulate(tableData, headers=heads, tablefmt="grid"))
    sp.plot(polSim, title="polinomio interpolante de hermite") 

def kpointsToArray(kpointsStr):
    kpointSplited = kpointsStr.split(",")
    kpoints = list(map(lambda x : float(x), kpointSplited ))
    return kpoints

p0 = float(eval(input("ingrese el valor a evaluar en el polinomio, si requiere, usar la libreria math: ")))
xpointStr = input("ingrese los puntos de x separados por , : ")
ypointStr = input("ingrese los puntos y separados por , : ")
ypPointStr = input("ingrese los puntos y' separados por , :")

polHermite(kpointsToArray(xpointStr), kpointsToArray(ypointStr), kpointsToArray(ypPointStr), p0)
