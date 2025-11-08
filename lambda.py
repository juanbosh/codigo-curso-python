# El lambda abrumador para el Short
def create_checker(divisor):
    """Crea una lambda para chequear la divisibilidad."""
    return lambda num: num % divisor == 0

# Lista de divisores y números
divisors = [2, 3, 5]
numbers = range(50)

# Un generator comprehension anidado y complejo
# para ver si los números son divisibles por alguno de los divisores
is_divisible = (
    lambda x, checks: 
    any(
        check(x) for check in checks
    )
) 

# Uso del lambda anidado en una list comprehension
results = [
    (n, is_divisible(n, [create_checker(d) for d in divisors]))
    for n in numbers
    if not(is_divisible(n, [create_checker(d) for d in divisors]))
]
print(results)

# El toque final: recursividad mal aplicada
# (Esto requiere un truco sintáctico o el operador morsa en Python reciente)
# Pero solo se muestra la lambda confusa:
# (Se rellena con comentarios si es necesario para llegar a 20 líneas)

# Final
# Demasiado abstracto.
# Muy poca recompensa visual.
# Requiere más de 60 segundos de explicación.
# Desliza para el siguiente Short...