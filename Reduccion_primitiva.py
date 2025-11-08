import time
from itertools import combinations

# --- Configuración y Ejecución ---

# Se establece el conjunto universal de números: del 1 al 14
numeros = list(range(1, 15))  

# Paso 1: Inicialización
# Genera todas las tripletas (combinaciones de 3) del conjunto base C(14, 3) = 364
tripletas = list(combinations(numeros, 3))  
# Usamos un 'set' (conjunto) para un seguimiento eficiente y operaciones rápidas de resta/intersección
tripletas_no_cubiertas = set(tripletas)  

# Lista que almacena el resultado final: las combinaciones de 6 seleccionadas
combinaciones_de_6 = []

# Inicia el tiempo
start_time = time.time()

# Paso 2: Bucle Voraz
# Itera mientras el conjunto de tripletas_no_cubiertas no esté vacío.
while tripletas_no_cubiertas:
    mejor_combinacion = None
    max_tripletas_cubiertas = 0

    # Paso 3: Búsqueda del Mejor Candidato (Procesamiento SECUENCIAL)
    # Itera sobre todas las posibles combinaciones candidatas de 6 números (C(14, 6) = 3003 candidatos).
    for combinacion_6 in combinations(numeros, 6):
        
        # Genera las tripletas contenidas en la combinación actual de 6 números.
        tripletas_en_combinacion = set(combinations(combinacion_6, 3))
        
        # Realiza la intersección (&): encuentra cuántas de las tripletas de esta combinación 
        # todavía están pendientes en el conjunto 'tripletas_no_cubiertas'.
        tripletas_cubiertas = tripletas_en_combinacion & tripletas_no_cubiertas  

        # Lógica Voraz: Si esta combinación cubre más tripletas que el máximo actual, se convierte en el nuevo mejor candidato.
        if len(tripletas_cubiertas) > max_tripletas_cubiertas:
            mejor_combinacion = combinacion_6
            max_tripletas_cubiertas = len(tripletas_cubiertas)

    # Si no se encontró ninguna tripleta adicional que cubrir (debería ser raro en este ejemplo)
    if mejor_combinacion is None or max_tripletas_cubiertas == 0:
        break
        
    # Paso 4: Actualización del Conjunto Cubriente
    # Agrega la mejor combinación greedy (la que cubre más) a la lista final.
    combinaciones_de_6.append(mejor_combinacion)
    
    # Actualiza el conjunto de tripletas pendientes: se restan (-) las tripletas que acaba de cubrir
    # la mejor_combinacion. Esta resta es extremadamente rápida gracias a los sets.
    tripletas_no_cubiertas -= set(combinations(mejor_combinacion, 3))

    # Imprime el progreso
    print(f"Combinación añadida: {mejor_combinacion} (Cubrió: {max_tripletas_cubiertas})")
    print(f"Tripletas restantes por cubrir: {len(tripletas_no_cubiertas)}")

# --- Resultado final ---
end_time = time.time()
execution_time = end_time - start_time
print("\n--- Resultado Final ---")
print(f"Número total de combinaciones de 6 necesarias: {len(combinaciones_de_6)}")
print("Combinaciones de 6 números:", combinaciones_de_6)
print(f"Tiempo total de ejecución: {execution_time:.2f} segundos")