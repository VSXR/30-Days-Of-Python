# EJEMPLO DE MATRICES EN PYTHON
matriz = [
   # C1 C2 C3
    [1, 2, 3], # Fila 0
    [4, 5, 6], # Fila 1
    [7, 8, 9]  # Fila 2
]

# FILAS --> variable i
# COLUMNAS --> variable j
# Recorremos las FILAS (Bucle Externo)
for i in range(len(matriz)):
    print(f"--- Entrando a la Fila {i} ---")
    
    # Recorremos las COLUMNAS de esa fila (Bucle Interno)
    for j in range(len(matriz[i])):
        valor = matriz[i][j]
        print(f"[Posicion ({i}, {j}): {valor}]", end=" ")
    
    # Al salir del bucle interno, hacemos un print vacío para saltar de línea
    print(f"\n--- Saliendo de la Fila {i} ---\n")


print("\n\n")


for i in range(1, 6):   # 5 FILAS
    for potencia in range(0, 4):    # 4 COLUMNAS: Empezamos como i^0, i^1, i^2, etc.
        if potencia == 0:           # En el caso de ser el primer numero de la FILA i, lo imprimimos (por eso son 5 numeros en vez de 4 del bucle for())
            print(f"{i}", end= " ")
        print(f"{i**potencia}", end=" ")
    print() # Salto de línea manual al terminar la fila completa
