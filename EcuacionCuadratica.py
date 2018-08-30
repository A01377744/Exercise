a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

x1 = (-b+((b**2)-(4*a*c))**(1/2))/(2*a)
x2 = (-b-((b**2)-(4*a*c))**(1/2))/(2*a)

print("Raíz 1= %.3f" % x1)
print("Raíz 2= %.3f" % x2)