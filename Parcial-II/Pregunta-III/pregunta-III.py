from itertools import combinations

def sublistas_crecientes(lista):
    yield []
    for i in lista:
        for sublista in combinations(lista, i): # Todas las posibles combinaciones de i nro de elementos de la lista
            if list(sublista) == sorted(sublista): # Ve si la sublista está ordenada
                yield list(sublista)

def main():
    lista = [1, 4, 3, 2, 5]
    lista1 = [5, 4, 3, 2, 1]
    lista2 = []

    print(f'lista: {lista}')
    for sublista in sublistas_crecientes(lista):
        print(sublista)
    print("\n")
    
    print(f'lista1: {lista1}')
    for sublista in sublistas_crecientes(lista1):
        print(sublista)
    print("\n")

    print(f'lista2: {lista2}')
    for sublista in sublistas_crecientes(lista2):
        print(sublista)
    

if __name__ == "__main__":
    main()