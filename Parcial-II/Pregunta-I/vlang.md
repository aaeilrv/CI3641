# V

**Pregunta I.a:**
Escoja algún lenguaje de programación de alto nivel y de propósito general cuyo nombre empiece con la misma letra que su apellido. Dé una breve descripción del lenguaje escogido:

1. De una breve descripción del lenguaje escogido.
    1. Enumere y explique las estructuras de control de flujo que ofrece.
        - Secuenciación:
        - Selección:
        - Iteración:
        - Abstracción Procedural:
        - Recursión:
        - Concurrencia:
        - Manejo de excepciones y especulación:
        - No-determinismo:

    2. Diga en qué orden evalúa expresiones y funciones.

        ### Expresiones binarias

        En V, la notación es infija para los operadores binarios. Asimismo, las expresiones se evalúan de izquierda a derecha y cumpliendo reglas de precedencia.

        Al igual que en la mayoría de los lenguajes, los paréntesis tendrán mayor prioridad ante todos los operadores.

        **Expresiones booleanas:**
        Se evalúan de izquierda a derecha, y la precedencia es la siguiente:
            2.  * / %
            1. + -
        
        ```
        println(1 + 4 / 4 * 2) // 3
        println(1 + 4 * 4 / 2) // 9
        ```

        - **Expresiones lógicas:**
        En el caso de los operadores lógicos, al usar más de uno nos pide hacer uso de paréntesis para asegurar el correcto orden de las operaciones:
        ```
        println(true || (false && true)) // true
        println(true || false && true) // error: expresiones booleanas ambiguas.
        ```

        **If:**
        A pesar de ser una declaración, también se puede utilizar como una expresión.
        ```
        num := 32
        valor := if num % 2 == 0 { 'par' } else { 'impar' }
        ```
        En este caso, es una notación infija multipalabra, se lee de izquierda a derecha siendo lo primero la condición que se debe cumplir y lo próximo los valores en caso de que se cumpla o no:
        ```
        resultado := if condicion { valor_si_verdadero } else { valor_si_falso }
        ```

        **Match:**
        Es una declaración parecida a utilizar un `if-else`, sin embargo, al igual que `if`, puede utilizarse como una expresión (en tal caso, no se puede utilizar en `for` loops ni expresiones `if`).
        Al utilizarse como una expresión, irá evaluando todos los casos de arriba a abajo hasta conseguir el caso donde hace match.
        ```
        const start = 1
        const end = 10
        c := 2

        num := match c {
            start...end {
                1000
            }
            else {
                0
            }
        }
        println(num) //1000
        ```

        **Pertenencia a arrays o maps:**
        Los operadores `in` e `!in `chequean si un valor está o no en un array o map. En caso de usarse en una expresión, retorna un booleano. Su escritura debe ser `[valor_a_buscar] in/!in [sitio_donde_buscar]`
        ```
        a := [1, 2, 3]
        b := 1 in a
        c := 1 !in a
        println(b) // true
        println(c) // false
        ```

        **Concatenación de strings:**
        Hace uso del operador `+` y el resultado será un string con los strings originales en orden de izquierda a derecha
        ```
        a := 'hola'
        b := 'profesor'
        println(a + b) // holaprofesor
        ```

        **Expresiones nivel de bit:**
        Evalúa de izquierda a derecha en el siguiente orden de precedencia:
            2.  &
            1.  |  ^
        ```
        println(12 ^ 10 & 8) // 4
        println(12 & 10 ^ 8) // 0
        ```

        ### Expresiones unarias
        La mayoría de las expresiones unarias son de tipo prefijo como `!` por el negado de una expresión booleana y `&` para obtener un valor por referencia.
        Al querer hacer un incremento o decremento del valor de una expresión numérica, será de tipo postfijo. Por ejemplo, V soporta `a++` mas no `++a`.

        **Funciones**
        En el caso de las funciones, el tipo viene después del nombre del argumento.
        Las funciones en V pueden ser utilizadas antes de su declaración, por lo que no se necesitan archivos de header

    3. Diga qué tipos de datos posee y qué mecanismos ofrece para la creación de nuevos tipos (incluyendo tipos polimórficos de haberlos).
        **Tipos Primitivos:**
        - bool
        - string
        - i8, i16, int, i64: enteros de tantos bits indique su nombre. `int` siempre será un entero de 32 bits
        - u8, u16, u32, u64: enteros sin signo (unsigned) de tantos bits indique su nombre.
        - f32, f64: flotante de 32 o 64 bits.
        - any (similar al void* de C)
        - voidptr: 
        - isize/usize: Indica cuántos bytes toma referenciar una ubicación en memoria, depende de la plataforma.

        Los valores como `18` o `3.15` son por default `int` y `f64` respectivamente.

        **Otros tipos de datos:**
        - Runes: representan un único caracter unicode. Para asignarlo se utilizan backticks `\`\`. Los mismos se pueden convertir en un string `UTF-8` haciendo uso del método `.str()` 

        **Arreglos:**
        Pueden ser de los siguientes tipos:
        Number	[]int,[]i64
        String	[]string
        Rune	[]rune
        Boolean	[]bool
        Array	[][]int
        Struct	[]MyStructName
        Channel	[]chan f64
        Function	[]MyFunctionType []fn (int) bool
        Interface	[]MyInterfaceName
        Sum Type	[]MySumTypeName
        Generic Type	[]T
        Map	[]map[string]f64
        Enum	[]MyEnumType
        Alias	[]MyAliasTypeName
        Thread	[]thread int
        Reference	[]&f64
        Shared	[]shared MyStructType 

        **Crear nuevo tipo de datos:**
        Para crear nuevos tipos de datos, se hace uso de `structs` de manera parecida a como se haría en lenguajes como C:
        ```
        Struct Persona {
            nombre string
            apellido string
        }

        mut alumno := Persona {
            nombre: 'valeria'
            apellido: 'vera'
        }

        println(alumno.nombre)
        ```

        **Conversión a otros tipo de datos:**
        Para la conversión a otros tipos, se utiliza la función de conversión de tipos: `T(v)`, con la que la variable `v` pasa a ser del tipo `T`.

    4. Describa el funcionamiento del sistema de tipos del lenguaje, incluyendo el tipo de equivalencia para sus tipos, reglas de compatibilidad y capacidades de inferencia de tipos.
