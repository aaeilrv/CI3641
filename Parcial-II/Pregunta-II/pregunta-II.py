precedencia = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}

no_conmutativo = set(['-', '/'])

### Funciones Auxiliares ###
def es_operador(token):
    operadores = set(['+', '-', '*', '/'])
    return token in operadores

def hacer_expresion(type, expresion):
    '''
    Asegura que los números negativos
    se lean correctamente
    '''
    if type == "POST":
        return expresion.split()
    elif type == "PRE":
        return expresion.split()[::-1]
    else:
        return "Tipo de expresión no válido. Use PRE o POST."

def ver_proximo_operador(pos, expresion):
    '''
    Devuelve el próximo operador de
    la expresion, si es que existe.
    '''
    i = pos + 1
    while i < len(expresion):
        if es_operador(expresion[i]):
            return expresion[i]
        i += 1
    return ""

def necesita_parentesis(a_evaluar, actual, posicion):
    if posicion == "primera_expresion":
        return precedencia[a_evaluar] < precedencia[actual]
    
    elif posicion == "segunda_expresion":
        return (precedencia[a_evaluar] < precedencia[actual] or
                precedencia[a_evaluar] == precedencia[actual] and
                actual in no_conmutativo)
    
def agg_parentesis(expresion):
    return f"({expresion})"

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
            if (i == '/') :
                i = '//'
            operando1 = stack.pop()
            operando2 = stack.pop()
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
            if (i == '/') :
                i = '//'
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
    for i in expresion:
        if es_operador(i):
            operando1, signo1 = stack.pop()
            operando2, signo2 = stack.pop()

            if signo1 and necesita_parentesis(signo1, i, 'primera_expresion'):
                operando1 = agg_parentesis(operando1)
            if signo2 and necesita_parentesis(signo2, i, 'segunda_expresion'):
                operando2 = agg_parentesis(operando2)

            stack.append((f"{operando1}{i}{operando2}", i))
        else:
            stack.append((i, None))
    return stack.pop()[0]

def mostrar_postfijo(expresion):
    stack = []
    for i in expresion:
        if es_operador(i):
            operando2, signo2 = stack.pop()
            operando1, signo1 = stack.pop()
            
            if signo1 and necesita_parentesis(signo1, i, 'primera_expresion'):
                operando1 = agg_parentesis(operando1)
            if signo2 and necesita_parentesis(signo2, i, 'segunda_expresion'):
                operando2 = agg_parentesis(operando2)

            stack.append((f"{operando1}{i}{operando2}", i))

        else:
            stack.append((i, None))
    return stack.pop()[0]

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