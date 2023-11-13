precedencia = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "": 0
}

### Funciones Auxiliares ###
def es_operador(token):
    operadores = set(['+', '-', '*', '/'])
    return token in operadores

def agg_parentesis(expresion):
    return f"({expresion})"

# Asegura que los números negativos se lean correctamente
def hacer_expresion(type, expresion):
    if type == "POST":
        return expresion.split()
    elif type == "PRE":
        return expresion.split()[::-1]
    else:
        return "Tipo de expresión no válido. Use PRE o POST."

def ver_proximo_operador(pos, expresion):
    i = pos + 1
    while i < len(expresion):
        if es_operador(expresion[i]):
            return expresion[i]
        i += 1
    return ""

def comparar_precedencia(actual, proximo):
    if precedencia[actual] < precedencia[proximo]:
        return True
    else:
        return False

### Evaluación ###
def evaluar_expresion(orden, expresion):
    exp = hacer_expresion(orden, expresion) 

    if orden == "PRE":
        return evaluar_prefijo(exp)
    elif orden == "POST":
        return evaluar_postfijo(exp)
    else:
        return "Orden no válido. Use PRE o POST."
    
def evaluar_prefijo(expresion):
    stack = []
    for i in expresion:
        if es_operador(i):
            operando1 = stack.pop()
            operando2 = stack.pop()
            print(operando1, i, operando2)
            resultado = eval(f"{operando1} {i} {operando2}")
            stack.append(resultado)
        else:
            stack.append(int(i))
    return stack.pop()

def evaluar_postfijo(expresion):
    stack = []
    for i in expresion:
        if es_operador(i):
            operando2 = stack.pop()
            operando1 = stack.pop()
            print(operando1, i, operando2)
            resultado = eval(f"{operando1} {i} {operando2}")
            stack.append(resultado)
        else:
            stack.append(int(i))
    return stack.pop()

### Mostrar ###
def mostrar_expresion(orden, expresion):
    exp = hacer_expresion(orden, expresion)
    if orden == "PRE":
        return mostrar_prefijo(exp)
    elif orden == "POST":
        return mostrar_postfijo(exp)
    else:
        return "Orden no válido. Use PRE o POST."

def mostrar_prefijo(expresion):
    stack = []

    for pos, i in enumerate(expresion):
        if es_operador(i):
            operando1 = stack.pop()
            operando2 = stack.pop()
            resultado = f"{operando1}{i}{operando2}"

            prox_ope = ver_proximo_operador(pos, expresion)

            # Agrega paréntesis si es necesario:
            if comparar_precedencia(i, prox_ope):
                resultado = agg_parentesis(resultado)             

            stack.append(resultado)
        else:
            stack.append(str(i))

    return resultado

def mostrar_postfijo(expresion):
    stack = []

    for pos, i in enumerate(expresion):
        if es_operador(i):
            operando2 = stack.pop()
            operando1 = stack.pop()
            resultado = f"{operando1}{i}{operando2}"

            prox_ope = ver_proximo_operador(pos, expresion)

            # Agrega paréntesis si es necesario:
            if comparar_precedencia(i, prox_ope):
                resultado = agg_parentesis(resultado)             

            stack.append(resultado)
        else:
            stack.append(str(i))


while True:
    action = input("Ingrese una acción (EVAL/MOSTRAR/SALIR): ").split()
    
    if action[0] == "EVAL":
        if len(action) < 3:
            print("Error: faltó información.")
            continue
        orden = action[1]
        expresion = " ".join(action[2:])
        resultado = evaluar_expresion(orden, expresion)
        print(resultado)
    elif action[0] == "MOSTRAR":
        if len(action) < 3:
            print("Error: faltó información.")
            continue
        orden = action[1]
        expresion = " ".join(action[2:])
        resultado = mostrar_expresion(orden, expresion)
        print(resultado)
    elif action[0] == "SALIR":
        break
    else:
        print("Acción no válida. Intente de nuevo.")