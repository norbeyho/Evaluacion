
numeros = []

for i in range(10):
    numero = float(input(f"Ingrese un número {i + 1}: "))
    numeros.append(numero)
    promedio = sum(numeros) / len(numeros)
print("El promedio de los numeros es:", promedio)


