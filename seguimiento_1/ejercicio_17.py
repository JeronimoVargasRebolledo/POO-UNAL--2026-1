import math

# ejercicio 17: área y longitud de circunferencia

print("Ingrese el radio del círculo:")
radio = float(input())

area = math.pi * (radio ** 2)
longitud = 2 * math.pi * radio

print("El área es:", area)
print("La longitud es:", longitud)
