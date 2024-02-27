import math
from tabulate import tabulate
import sympy as sp

heads = ["i", "p"]
tableData = []
x = sp.Symbol('x')
def newton(p0, tol, n, f):
    i = 1
    ff = sp.lambdify(x, f)
    while i <= n:
        df = sp.diff(f, x)
        dff = sp.lambdify(x, df)
        p = p0 - ff(p0)/dff(p0)
        tableData.append([i, p])
        if abs(p - p0) < tol:
            break
        i += 1
        p0 = p
    print(tabulate(tableData, headers = heads, tablefmt = "grid"))  


p0 = float(eval(input("ingrese la aproximacion inicial con modulo math, si requiere: ")))
tol = float(input("ingrese la tolerancia: "))
n = int(input("ingrese el numero de iteraciones: "))
f = eval(input("ingrese la funcion usando sympy, ejemplo: 'sp.cos(x)' -->  "))   
newton(p0, tol, n, f)

