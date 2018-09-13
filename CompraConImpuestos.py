#Autores: Silvia Ferman, Alejandro Torices
#Calcular el subtotal, los impuestos federal y estatal y el total.
#Demo Top-Down

def calcularImpuestoF(subtotal):
    federal = subtotal * .17
    return federal

def calcularImpuestoE(subtotal):
    estatal = subtotal * .04
    return estatal
def imprimir(subtotal, total, federal, estatal):
    print("El subtotal es: %.2f" % subtotal)
    print("El impuesto federal es: %.2f" % federal)
    print("El impuesto estatal es: %.2f" % estatal)
    print("El total es: %.2f" % total)

def main():
    subtotal = int(input("El subtotal de la compra es: "))
    federal = calcularImpuestoF(subtotal)
    estatal = calcularImpuestoE(subtotal)
    total = subtotal + federal + estatal
    imprimir(subtotal, total, federal, estatal)

main()