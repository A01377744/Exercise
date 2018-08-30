#Autor: Alejandro Torices Oliva
#Dibuja un triángulo dad su altura e imprime área y perímetro.
#Demo de Top-Down

import math #para cos
import turtle

def calcularLado(altura):
    lado = altura / math.cos(30*math.pi / 180) #O math.radians(30)
    return lado

def dibujarTriangulo(lado):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    tortuga.left(120)
    turtle.exitonclick()

def dibujar(altura):
    lado = calcularLado(altura)
    dibujarTriangulo(lado)

def main():
    altura = int(input("Teclea la altura: "))
    dibujar(altura)


#Llama a la función main
main()