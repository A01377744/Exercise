#Autor: Alejandro Torices Oliva
#Prueba funciones con la instruccion if

def buscarMayor(a, b):
    if a > b:
        return a
    else:
        return b


#Otra forma de escribir la función.
"""
def buscarMayor(a,b):
    if a>b:
        return a
    
    return b """


def buscarMayor(a, b, c):
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c


def buscarMayorDos(a, b, c, d):
    mayorUno = buscarMayor(a, b)
    mayorDos = buscarMayor(c, d)
    mayor = buscarMayor(mayorUno, mayorDos)
    return mayor

def main():
    a = int(input("Valor 1:"))
    b = int(input("Valor 2:"))
    c = int(input("Valor 3:"))
    d = int(input("Valor 4:"))
    mayor = buscarMayorDos(a, b, c, d)
    print("El mayor es: ", mayor)

main()