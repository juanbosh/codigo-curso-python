from functools import wraps

def medir_tiempo(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado

    return wrapper

@medir_tiempo
def suma_numeros(n):
    total = 0
    for i in range(n):
        total += i
    return total 

if __name__ == "__main__":
    n = 1000000
    resultado = suma_numeros(n)
    print(f"La suma de los primeros {n} números es: {resultado}")   