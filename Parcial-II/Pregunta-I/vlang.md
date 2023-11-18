# Vlang

**Pregunta I.a:**
Escoja algún lenguaje de programación de alto nivel y de propósito general cuyo nombre empiece con la misma letra que su apellido. Dé una breve descripción del lenguaje escogido:

1. De una breve descripción del lenguaje escogido.
    1. Enumere y explique las estructuras de control de flujo que ofrece.

        - **Secuenciación:**
        Vlang no hace uso de `;` ni ningún símbolo como terminador de instrucción o de declaración. Por ende, para toda nueva declaración se debe hacer un salto de línea.

        Para declarar bloques de instrucciones, se hace uso de los corchetes `{}` como delimitantes de cuáles instrucciones, declaraciones, etc. serán parte del bloque.

        - **Selección:**
        En V se hace uso de los `if`, `else if` y `else` típicos de varios lenguajes de programación. No hay paréntesis rodeando la expresión.

        ```
        n := 100

        if 0 < n < 10 {
            println('Ejemplo de if')
        } else if n >= 10 {
            println('Ejemplo de else if')
        } else {
            println('Ejemplo de else')
        }
        ```

        A su vez, existe la declaración `match`, que es una manera corta de escribir un `if-else`. Cuando consigue una rama donde hace match, sigue el bloque de declaraciones que le sigue:

        ```
        nombre := 'Valeria'
        println('¿Es ${nombre} estudiante?')
        match nombre {
            'Valeria' { println('Si es estudiante') }
            'Ricardo' { println('No! Es profesor') }
            else { println('no sabemos') }
        }
        ```

        - **Iteración:**
        Para iterar, V únicamente ofrece el keyword `for`. Sin embargo, existen distintas maneras en las que puede ser usada:
            1. `for`/`in`:
            Se puede utilizar con un array, map o rango numérico para iterar sobre los elementos de los mismos:
            ```
            // Array
            numbers := [1, 2, 3, 4, 5]
            for number in numbers {
                println(number)
            }

            // Map
            m := {
                'uno': 1
                'dos': 2
            }
            for key, value in m {
                println('${value} -> ${key}')
            }

            /* Al sólo querer uno de los dos elementos, se puede hacer
            for _, value in m {} o for key, _ in m{} */

            // Rango numérico
            for i in 0..5 {
                println(i)
            }
            ```

            2. `for` de condición: Iterará hasta que la condición se vuelva falsa.
            ```
            mut sum := 0
            mut i := 0
            for i <= 10 {
                sum += i
                i++
            }
            ```

            3. `for` sin condición: Se omite la condición resultado en un loop infinito hasta que se
            haga un `break` o `continue`
            Parecido a un `while(true)`

            ```
            mut num := 0
            for {
                num += 2
                if num >= 10 {
                    break
                }
            }
            ```

            4. `C for`: Como sabemos, Vlang toma muchas cosas prestadas de C. Entre ellas, su `for` de condición:
            ```
            for i := 0; i < 10; i++ {
                println(i)
            } 
            ```

        - **Abstracción Procedural:**
        V permite definir funciones y procedimientos, ambos de la misma manera `fn nombre() {[bloque de instrucciones]}`.
        En el caso de las funciones, las mismas pueden retonar múltiples valores. Para ello, deben ser separados por una coma.

        ```
        fn funcion() {
            return 5, 6
        }

        int main() {
            a, b := funcion()
            println(a) // 5
            println(b) // 6
        }
        ``` 

        - **Recursión:**
        Para hacer una recursión segura, se debe utilizar `sum types`, lo cual es una instancia que toma un valor que puede ser de distintos tipos. (explicado mejor más adelante).

        ```
        struct Cero {}

        struct Succ {
            prev Church
        }

        type Church = Cero | Succ
        ```

        Otra manera de hacer recursión, en especial cuando se necesitan hacer estructuras como árboles binarios, listas enlazadas, o cualquier struct con referencias, es utilizar punteros a `nil`. Sin embargo, la documentación de Vlang explica que esto es **unsafe** y no recibirá soporte en el futuro.

        ```
        struct Nodo {
	    valor f64
        mut:
            izq  &Nodo = unsafe { nil }
            der  &Nodo = unsafe { nil }
        }
        ```

        Estos campos deben ser inicializados a menos que se haya declarado un valor inicial
        ```
        mut raiz := {10, 0, 0}
        ```

        - **Concurrencia:**
        De acuerdo a la propia documentación de Vlang, su modelo de concurrencia es bastante similar al de Go. 
        Para correr una subrutina `p()` concurrentemente en otro hilo, se debe ejecutar `spawn p()`:

        ```
        fn p() {
            println('ejemplo')
        }

        spawn q() {
            println('otra manera de correr una subrutina concurrentemente en otro hilo.')
        }

        fn main() {
            spawn p()
        }
        ```

        Para esperar a que termine la ejecución en un hilo paralelo o para obtener el valor de retorno de una función corriendo en un hilo paralelo, se utiliza `wait()`:

        ```
        fn p() {
            return 3
        }

        fn main() {
            x := spawn p()
            x.wait() // Terminó la ejecución de p

            y := spawn p()
            z := y.wait() // Obtiene el valor de retorno de p
            println(z) // Imprime el valor de retorno de p
        }

        ```

        - **Manejo de excepciones y especulación:**

        V no maneja excepciones con los bloques `throw/try/catch`.

        Para levantar errores, se hace uso de la función `error()` que permite agregar un mensaje de error.

        Para manejar un error, hay diversos métodos de hacerlo:

            1. Terminar temprano la ejecución: ya sea con `exit()` o `panic()` que detienen la ejecución de todo el programa, o a través de una declaración del control de flujo como `return`, `break` o `continue`.

            2. Propagar el error.

            3. proveer un valor default al final de un bloque `or`. En el caso de un error, ese sería el valor asignado:

            ```
            fn do_something(s string) !string {
                if s == 'foo' {
                    return 'foo'
                }
                return error('invalid string')
            }

            a := do_something('foo') or { 'default' } // a will be 'foo'
            b := do_something('bar') or { 'default' } // b will be 'default'
            println(a)
            println(b)
            ```

            4. `if` unwrapping.

        Además. también se pueden definir tipos de error personalizados haciendo uso de la interfaz IError.

        En caso de testing, usualmente se utiliza `assert`:
        	- Para chequear si una expresión evalúa a `true`, se hace uso de `assert`. Generalmente, si el assert falla, el programa es abortado.
            - Si no se desea que el programa aborte, se debe hacer uso de la etiqueta `[assert_continues]`.

            ```
            @[assert_continues]
            fn abc(ii int) {
                assert ii == 2
            }

            for i in 0 .. 4 {
                abc(i)
            }
            ```
            Generará el siguiente output:
            ```
            assert_continues_example.v:3: FAIL: fn main.abc: assert ii == 2
            left value: ii = 0
            right value: 2
            assert_continues_example.v:3: FAIL: fn main.abc: assert ii == 2
            left value: ii = 1
            right value: 2
            assert_continues_example.v:3: FAIL: fn main.abc: assert ii == 2
            left value: ii = 3
            right value: 2
            ```

        - **No-determinismo:**
        V no es nodeterminista por definición. Sin embargo, al hacer uso de hilos puede comportarse de manera nodeterminista si los mismos no están sincronizados.

    2. Diga en qué orden evalúa expresiones y funciones.

        ### Expresiones binarias

        En Vlang, la notación es infija para los operadores binarios. Asimismo, las expresiones se evalúan de izquierda a derecha y cumpliendo reglas de precedencia.

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
        Mismo caso de If, donde se puede utilizar como una expresión y el valor guardado será aquel que haga *match* con el caso. Se lee de arriba a abajo hasta hacer el *match*.
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

        ### Funciones
        En el caso de las funciones, el tipo viene después del nombre del argumento.

        Se pueden definir funciones propias de un interface, struct o type, esto para poder llamar `i.funcion()` en vez de `funcion(i)`. Resulta conveniente si se requiere hacer una función con el mismo nombre pero para diversos tipos de parámetros:

        ```
        struct Cat {}
        struct Dog {}

        fn (c Cat) talk() {
            println("meow")
        }

        fn (d Dog) talk() {
            println("woof")
        }

        fn main() {
            cat := Cat{}
            dog := Dog{}
            
            cat.talk()
            dog.talk()
        }
        ```

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

        **Arreglos:**
        Pueden ser de los siguientes tipos:
        
        | Tipo | Ejemplo de definición |
        | ---------------|----------------------- |
        | Number | []int,[]i64 |
        | String | []string |
        | Rune | []rune |
        | Boolean | []bool |
        | Array | [][]int |
        | Struct | []MyStructName |
        | Channel | []chan f64 |
        | Function | []MyFunctionType []fn (int) bool |
        | Interface | []MyInterfaceName |
        | Sum Type | []MySumTypeName |
        | Generic Type | []T |
        | Map | []map[string]f64 |
        | Enum | []MyEnumType |
        | Alias | []MyAliasTypeName |
        | Thread | []thread int |
        | Reference | []&f64 |
        | Shared | []shared MyStructType |

        **Otros tipos de datos:**
        - Runes: representan un único caracter unicode. Para asignarlo se utilizan backticks `\`\`. Los mismos se pueden convertir en un string `UTF-8` haciendo uso del método `.str()` 
        - Maps: implementan una tabla de hash. Puede tener keys del tipo string, rune, integer, float o voidptr

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

        Además, también se pueden usar `sum types`, los cuales son instancias que pueden tener valores de distintos tipos:
        ```
        struct Perro {}
        struct Gato {}
        
        type Animal = Perro | Gato
        ```

    4. Describa el funcionamiento del sistema de tipos del lenguaje, incluyendo el tipo de equivalencia para sus tipos, reglas de compatibilidad y capacidades de inferencia de tipos.

    El tipo de las variables es inferido del valor en el lado derecho. En caso de querer utilizar otro tipo, se utiliza la función de conversión de tipos: `T(v)`, con la que la variable `v` pasa a ser del tipo `T`:
    ```
    a := 23 //Int
    b := i16(23) //i16
    ```

    En V, todos los operadores deben ser del mismo tipo en ambos lados, es decir, algo como esto no está permitido:
    ```
    mut a := 'hola'
    println(a + 3)
    ```
    Sin embargo, existe una excepción en el caso de los integers y unsigned, donde un tipo primitivo pequeño puede ser promovido si cabe por completo en el data range del otro tipo. Para saber todas las posibilidades, nos guiamos de esta tabla:
    ```
        i8 → i16 → int → i64
                    ↘     ↘
                    f32 → f64
                    ↗     ↗
        u8 → u16 → u32 → u64 ⬎
            ↘     ↘     ↘      ptr
        i8 → i16 → int → i64 ⬏
    ```
    Para entender la idea mejor, se da un ejemplo de la promoción de tipos:
    ```
    a := 47 // int por default
    b := u16(56) // u16
    c := a + b // c es de tipo int, se hizo una promoción de b.
    ```
    ```
    x := 3.14 // f64 por default
    y := f32(1.6)
    z := x - y //z es de tipo f64, se hizo una promoción de y.
    ```

    En el caso de los `sum types`, Para asegurarse de qué tipo es, se utiliza `is`. Para pasar de uno de sus tipos a otro, se utiliza `as`:

        ```
        struct Perro {}
        struct Gato {}
        
        type Animal = Perro | Gato

        fn (g Gato) rasguno() bool {
            return true
        }

        fn main() {
            mut x := Animal(Perro{})
            assert x is Perro // Se asegura del tipo

            x = Gato{}

            gato := x as Gato // Se accede a la instancia Gato
            if gato.rasguno() {
                println('Me ha rasgunado!')
            }
        }
        ```

**Pregunta I.b:**
v run church.v

**Pregunta I.c:**
v run arbol.v