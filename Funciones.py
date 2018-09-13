#Autor: Alejandro Torices Oliva
#Ejemplos de uso de funciones

import turtle               #Importa una librería

def main():
    print("Hola")
    print("Mundo")

def dibujarCuadro(tortuga):
    tortuga.forward(200)
    tortuga.left(90)       #Gira 90° a la izquierda
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)

#Llamada a la función
tA = turtle.Turtle()
tA.shape("circle")
tA.pencolor("blue")
dibujarCuadro(tA)

tA.penup()
tA.goto(-200,-200)
tA.pendown()
dibujarCuadro(tA)

tA.penup()
tA.goto(0,-200)
tA.pendown()
dibujarCuadro(tA)

tA.penup()
tA.goto(-200,-0)
tA.pendown()
dibujarCuadro(tA)

tA.penup()
tA.goto(0,0)
tA.pendown()
tA.left(45)
dibujarCuadro(tA)

tA.left(90)
dibujarCuadro(tA)
tA.left(90)
dibujarCuadro(tA)
tA.left(90)
dibujarCuadro(tA)

#Para que no cierre la ventana
turtle.exitonclick()