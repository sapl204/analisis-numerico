import math
from tabulate import tabulate

head = ["i", "p"]
tableData = []
def biseccion(a, b, n, tol, f):
    if f(a)*f(b) > 0:
        print(f"no hay ceros en: [${a}, ${b}]")
    else:
        i = 1
        fa = f(a)

        while i <= n:
            p = (a+b)/2
            tableData.append([i , p])
            fp = f(p)
            if fp == 0 or (b-a)/2 < tol:
                break
            i += 1
            if fp*fa > 0:
                a = p
                fa = fp
            else:
                b = p
        print(tabulate(tableData, headers = head, tablefmt = "grid" ))


print("Si se van a usar funciones matematicas fuera del alcance de python en este archivo, usar math")
a = float(eval(input("ingrese el extremo izquierdo del intervalo: ")))    
b = float(eval(input("ingrese el extremo derecho del intervalo: ")))
n = int(input("numero de interaciones: "))  
tol = float(input("ingrese la tolerancia: "))
f = eval(input("ingrese la funcion usando lambda, ejemplo, lambda x: math.cos(x) - x --> "))
biseccion(a, b, n, tol, f)  
        
