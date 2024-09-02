# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = 0
suma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero
else:       
        suma_impares += numero

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")  
