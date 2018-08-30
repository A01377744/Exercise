a = int(input("Teclea la medida a: "))
b = int(input("Teclea la medida b: "))
c = int(input("Teclea la medida c: "))
d = int(input("Teclea la medida d: "))

areaRectangulo =(a-c-d)*b

areaTrianguloIzq = (d*b)/2

areaTrianguloDer = (c*b)/2

areaTotal = areaRectangulo + areaTrianguloIzq + areaTrianguloDer

costo = areaTotal * 3450

print("El area total es: ", areaTotal)
print("El costo es: $", costo)