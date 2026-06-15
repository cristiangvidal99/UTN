#pedimos al usuario que ingrese los datos

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)

# pinto el resultado y lo redondeo
print("Resultado:", round(resultado, 2))

