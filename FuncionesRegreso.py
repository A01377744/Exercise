#encoding: UTF-8
#Autor: Alejandro Torices Oliva
#Muestra como trabajan las funciones que reciben y regresan datos

#Recibe puntos (HP) y regresa la calificación (0-100)
#2505 HP es 100 de calificación

def calcularCalificacion(hp):
    calificacion = hp * 100 / 2505
    return (calificacion)

#Recibe la edad y meses enteros de una persona y regresa los días vividos
def calcularDias(a, m):
    dias = a*365 + m*30
    dias = a//4 + dias
    return dias

#Principal, resuelve el problema
def main():
    nA = int(input("Años: "))
    nM = int(input("Meses: "))
    totalDias = calcularDias(nA, nM)
    print("Has vivido ", totalDias, "dias")

"""
def main():
    puntos = int(input("Cuántos HP quieres transformar? "))
    resultado = calcularCalificacion(puntos)
    print("%d hp equivalen a %.1f de calificación" % (puntos, resultado))
"""
#Llamar a la función main

main()