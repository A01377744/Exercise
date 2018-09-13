
import math

def buscarMayor(a, b, c):
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c
def main():
    a = int(input("Introduce el valor de a: "))
    b = int(input("Introduce el valor de b: "))
    c = int(input("Introduce el valor de c: "))
    hipotenusa = buscarMayor(a, b, c)


