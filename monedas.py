#Autor: Alejandro Torices Oliva, A01377744, ISC
#Programa que recibe los puntos obtenidos y el nivel completado y despliega el número de monedas ganadas,
# y/o el número de estrellas ganadas y la clasificación del jugador sólo si está en la última categoría.


#Recibe la cantidad de puntos obtenidos y regresa las monedas ganadas.
def obtenerMonedas(puntos):
    if puntos >= 0 and puntos <= 75:
        return 0
    elif puntos > 75 and puntos <= 150:
        return 2
    elif puntos > 150 and puntos <= 350:
        return 5
    elif puntos > 350 and puntos <= 400:
        return 7
    else:
        return 8


#Recibe las monedas ganadas y el nivel superado y regresa las estrellas ganadas.
def obtenerEstrellas(monedas, nivel):
    if monedas == 7:
        if nivel < 5:
            return "También gana 1 estrella."
        else:
            return "También gana 3 estrellas."
    if monedas == 8:
        if nivel <=3:
            return "También gana 2 estrellas."
        else:
            return "También gana 5 estrellas."
    else:
        return 0


#Recibe las monedas ganadas y regresa la clasificación solo si está en la última categoría.
def calcularClasificacion(monedas):
    if monedas == 8:
        return "Clasificación: Profesional"
    else:
        return 0


#Función principal.
def main():
    print("2do. Examen, Alejandro Torices Oliva, A01377744")
    print("")

    puntosObtenidos = int(input("Puntos obtenidos: "))
    nivelTerminado = int(input("Nivel terminado: "))
    print("")

    monedas = obtenerMonedas(puntosObtenidos)
    estrellas = obtenerEstrellas(monedas, nivelTerminado)
    clasificacion = calcularClasificacion(monedas)

    print("El jugador gana %d monedas. " % (monedas))
    if estrellas != 0:
        print(estrellas)
    if clasificacion != 0:
        print(clasificacion)
    print("")

    print("Termina programa.")


main()