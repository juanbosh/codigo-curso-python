#!/usr/bin/env python3
from itertools import combinations
import sys

solucion = [
    (1, 2, 3, 4, 5, 6), (1, 2, 7, 8, 9, 10), (1, 2, 11, 12, 13, 14),
    (3, 4, 7, 8, 11, 12), (3, 4, 9, 10, 13, 14), (5, 6, 7, 8, 13, 14),
    (5, 6, 9, 10, 11, 12), (1, 3, 5, 7, 9, 11), (1, 3, 5, 8, 10, 12),
    (1, 4, 6, 7, 9, 12), (1, 4, 6, 8, 10, 11), (2, 3, 6, 7, 10, 11),
    (2, 3, 6, 8, 9, 12), (2, 4, 5, 7, 10, 12), (2, 4, 5, 8, 9, 11),
    (1, 2, 3, 5, 13, 14), (1, 2, 4, 6, 13, 14), (1, 2, 7, 9, 13, 14),
    (1, 2, 8, 10, 13, 14), (3, 4, 7, 11, 13, 14), (3, 4, 8, 12, 13, 14),
    (5, 6, 9, 11, 13, 14), (5, 6, 10, 12, 13, 14), (7, 8, 9, 12, 13, 14),
    (7, 8, 10, 11, 13, 14), (3, 4, 5, 6, 13, 14)
]

def main():
    todas = set(combinations(range(1, 15), 3))
    cubiertas = set()
    for comb in solucion:
        cubiertas.update(combinations(comb, 3))

    faltantes = sorted(todas - cubiertas)
    print(f"Total tripletas: {len(todas)}")
    print(f"Cubiertas: {len(cubiertas)}")
    print(f"NO cubiertas: {len(faltantes)}")

    if faltantes:
        print("\n❌ SOLUCIÓN INVÁLIDA")
        print(f"Faltan {len(faltantes)} tripletas. Mostrando hasta 50:")
        for t in faltantes[:50]:
            print(t)
        sys.exit(1)
    else:
        print("\n✅ SOLUCIÓN VÁLIDA")
        sys.exit(0)

if __name__ == "__main__":
    main()