import math
from tabulate import tabulate

head = ["i", "p", "error"]
tableData = []
def puntofijo(p0, n, tol, g):
    i = 1
    while i <= n:
        p = g(p0)
        tableData.append([i, p, abs(p - p0)])
        if abs(p-p0) < tol:
            break
        i += 1
        p0 = p
    print(tabulate(tableData, headers = head, tablefmt = "grid"))


print("Si se van a usar funciones matematicas fuera del alcance de python en este archivo, usar math")
p0 = float(eval(input("ingrese la aproximaciòn inicial: ")))
n = int(input("numero de iteraciones: "))
tol = float(input("ingrese la tolerancia: "))
g = eval(input("ingrese la funcion de punto fijo en lambda, ejemplo, lambda x: math.cos(x) - x --> "))
puntofijo(p0, n, tol, g)
