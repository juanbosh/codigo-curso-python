import asyncio
import time

# --- 1. Función Asíncrona con Tiempo de Espera Variable ---
async def descargar_datos(sitio_web, tiempo_espera):
    """
    Simula la descarga de datos de un sitio web.
    Usa asyncio.sleep() para simular el tiempo de espera por la red (I/O).
    """
    print(f"[{time.strftime('%H:%M:%S')}] 🟡 Comenzando la descarga de {sitio_web} (espera: {tiempo_espera}s)")
    
    # El 'await' aquí cede el control al bucle de eventos.
    # Esto permite que la Tarea 2 y la Tarea 3 comiencen mientras esta espera.
    await asyncio.sleep(tiempo_espera) 
    
    print(f"[{time.strftime('%H:%M:%S')}] ✅ Terminada la descarga de {sitio_web}")
    return f"Resultado de {sitio_web}: Datos listos."

# --- 2. Función Principal (El Orquestador) ---
async def main_complejo():
    inicio = time.monotonic()
    print(f"[{time.strftime('%H:%M:%S')}] 🚀 Iniciando la orquestación de tareas...")
    
    # Creamos las corrutinas que queremos ejecutar concurrentemente
    tarea_1 = descargar_datos("Servidor-A", 5) # Lenta
    tarea_2 = descargar_datos("Servidor-B", 8) # La más lenta (será el tiempo total)
    tarea_3 = descargar_datos("Servidor-C", 2) # Rápida

    # asyncio.gather() ejecuta todas las corrutinas *al mismo tiempo* (concurrentemente)
    # y espera a que *todas* terminen. Devuelve una lista con los resultados.
    resultados = await asyncio.gather(tarea_1, tarea_2, tarea_3)
    
    fin = time.monotonic()
    
    print("-" * 30)
    print("✨ Resultados de las Tareas:")
    for res in resultados:
        print(f"- {res}")
    print(f"\n⏱️ Tiempo total de ejecución: {fin - inicio:.2f} segundos.")
    print(f"(La suma de esperas es: 5 + 8 + 2 = 15 segundos)")

# --- 3. Ejecución (Punto de Entrada) ---
if __name__ == "__main__":
    # asyncio.run() se encarga de crear el bucle de eventos y ejecutar
    # nuestra función 'main' en él.
    asyncio.run(main_complejo())