#Autor: Alejandro Torices Oliva
#Prueba instrucción if, if-else

def main():
    """numero = int(input("Número: "))
    doble = 2 * numero
    print("El doble es ", doble)

    if doble%6 == 0:
        print("Número afortunado.")"""
    carrera = input("Carrera:")

    if carrera.upper() == "INT":
        print("Estás en el salón equivocado.")
    else:
        print("Estás en el salón correcto.")

main()