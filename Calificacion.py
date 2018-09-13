#Autor: Alejandro Torices Oliva
#Prueba funciones con la instruccion if

def determinarValidez(calificacion):
    if 0<= calificacion <=100:
        if calificacion < 70:
            return "Reprobado"
        return "Aprobado"
    return "Error"

def main():
    calificacion = float(input("Ingrese la calificación: "))
    determinarValidez(calificacion)
    print(determinarValidez(calificacion))

main()