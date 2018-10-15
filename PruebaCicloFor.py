#Autor: Alejandro Torices Oliva
#Prueba ciclo for

def imprimirNombre(n):
    for vuelta in range(n):     #Genera n valores
        print("Alejandro Torices")

def imprimirTabla7():
    for factor in range(1,11):          #[1,2,..10]
        producto = 7 * factor
        print("7 x %d = %d" % (factor, producto))

def imprimirTabla(tabla):
    print("Tabla del", tabla)
    for factor in range(1,11):
        producto = tabla * factor
        print(tabla, "x" , factor, "=", producto)

def main():
    for tabla in range(1,11):
        imprimirTabla7()
    #imprimirNombre(5)



main()