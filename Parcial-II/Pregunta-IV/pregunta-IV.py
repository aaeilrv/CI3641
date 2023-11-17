# alpha = 3, beta = 4
import time

def subrutina_recursiva(n):
    if 0 <= n < 12:
        return n
    if n >= 12:
        return subrutina_recursiva(n - 4) + subrutina_recursiva(n - 8) + subrutina_recursiva(n - 12)

def recursion_de_cola(n):
    def aux_cola(n, acumulador = 0):
        if n == 0:
            return acumulador
        else:
            return aux_cola(n - 1, acumulador + calculate_tribonacci(n))
    return aux_cola(n)

def subrutina_iterativa(n):
    acumulador = 0
    while n > 0:
        acumulador += calculate_tribonacci(n)
        n -= 1
    return acumulador

def tribonacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        a, b, c = 1, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c

        return c

def calculate_tribonacci(n):
    '''
    Para calcular el número de tribonacci a usar.
    '''
    base = 3
    intervalo_de_repeticion = 4
    offset = 13 

    if n == 0:
        return tribonacci(0)
    if 0 < n < offset:
        return tribonacci(1)

    return tribonacci(base + ((n - offset) // intervalo_de_repeticion))

def main():

    tiempos_recursion_simple = []
    tiempos_recursion_de_cola = []
    tiempos_iteracion = []

    valor = 100

    for i in range(0, 11):
        start = time.time()
        subrutina_recursiva(valor)
        end = time.time()
        tiempos_recursion_simple.append((end - start) * 1000)

        start = time.time()
        recursion_de_cola(valor)
        end = time.time()
        tiempos_recursion_de_cola.append((end - start) * 1000)

        start = time.time()
        subrutina_iterativa(valor)
        end = time.time()
        tiempos_iteracion.append((end - start) * 1000)

    tiempos_recursion_simple = sum(tiempos_recursion_simple) / len(tiempos_recursion_simple)
    tiempos_recursion_de_cola = sum(tiempos_recursion_de_cola) / len(tiempos_recursion_de_cola)
    tiempos_iteracion = sum(tiempos_iteracion) / len(tiempos_iteracion)

    print(f'recursión simple: {tiempos_recursion_simple}')
    print(f'recursión de cola: {tiempos_recursion_de_cola}')
    print(f'iteración: {tiempos_iteracion}')

if __name__ == "__main__":
    main()