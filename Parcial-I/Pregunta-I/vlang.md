# V


**Pregunta I.a:**
Escoja algún lenguaje de programación de alto nivel y de propósito general cuyo nombre empiece con la misma letra que su nombre. Dé una breve descripción del lenguaje escogido:

1. Diga qué tipo de alcances y asociaciones posee, argumentando las ventajas y desventajas de la decisión tomada por los diseñadores del lenguaje, en el contexto de sus usuarios objetivos.

Vlang tiene alcance estático o léxico. Además, su asociación es superficial.
Dado a que V es similar a Go e influenciado por Oberon, Rust, Swift, Kotlin y Python, no posee mayor dificultad a la hora de ser aprendido.

2. Diga qué tipo de módulos ofrece (de tenerlos) y las diferentes formas de importar y exportar nombres.
V permite el uso de módulos como librería que pueden ser reusables. (X)[https://github.com/vlang/v/blob/master/doc/docs.md#modules] Para crearlos, se debe hacer en un nuevo directorio con el nombre del módulo a crear donde se contengan todos los archivos .v que el módulo necesite:
```
module mymodule

pub fn test_1() {
	println("Esto es un test.")
}
```
El alcance de estos módulos es de tipo cerrado, puesto que los nombres se deben importar de la siguiente manera:
```
import mymodule

fn main() {
	mymodule.test_1()
}
```
Sin embargo, se pueden importar funciones específicas de los módulos o utilizar aliases para los tipos (X)[https://codeberg.org/NoNamePro0/vlang/src/branch/master/doc/docs.md#user-content-modules].

```
import time

type MyTime = time.Time

fn (mut t MyTime) century() int {
    return 1 + t.year % 100
}
```

3. Diga si el lenguaje ofrece la posibilidad de crear aliases, sobrecarga y polimorfismo. En caso afirmativo, dé algunos ejemplos

### Aliases ###
V permite crear aliases para tipos existentes [x](https://github.com/vlang/v/blob/master/doc/docs.md#type-aliases), por ejemplo:

```
type Ante = int

struct Example {
	estudi Ante
}

fn example_sum(gig Ante, brill Ante) {
	println(gig + brill)
}

fn main() {
	ex := Example{
		estudi: 1
	}
	example_sum(ex.estudi, 2)
}
```


### Sobrecarga ###
V no permite el uso de sobrecargas en funciones para mantener la simplicidad y legibilidad. Sin embargo, si permite sobrecarga de operadores únicamente para `+, -, *, /, %, <, ==`[X](https://github.com/vlang/v/blob/master/doc/docs.md#limited-operator-overloading). Aún así, mantiene algunas restricciones:
- Cuando se sobrecarga `<` o `==`, el retorno debe ser estrictamente de tipo `bool`
- Ambos argumentos deben ser del mismo tipo
- Los argumentos no pueden ser cambiados dentro de la sobrecarga
- No se puede llamar a otras funciones dentro de la función donde se hace la sobrecarga.

```
struct Vec {
	x int
	y int
}

fn (a Vec) + (b Vec) Vec {
	return Vec{a.x + b.x, a.y + b.y}
}

fn main() {
	a := Vec{2, 3}
	b := Vec{4, 5}

	println(a + b)
}
```
### Polimorfismo ###
Actualmente, V no ofrece la posibilidad de crear polimorfismos.

4. Diga qué herramientas ofrece a potenciales desarrolladores, como: compiladores, intérpretes, debuggers, profilers, frameworks, etc.
### Compiladores ###
- V es un lenguaje compilado que además puede a su vez compilarse en C. Esto lo hace pasando el código fuente en un árbol de síntesis abstracta (AST) que, una vez creado, permite obtener con el backend de C (`vlib/gen/c`) un archivo temporal en C. Por último, se llama al compilador de C y se genera el binario. Para este proceso, se debe ejecutar `v -o file.c your_file.v` para generar un archivo en C correspondiente al código en V.
- El compilador de V fue escrito en él mismo. Para ello, se utilizó la técnica de bootstrapping en Go hasta que finalmente pudiese compilarse a él mismo. [Fuente](https://github.com/vlang/v/discussions/17308)
- Existen varios compiladores escritos en V como vcc (compilador de C escrito en V), Vork (compilador de V escrito en Python), vas (ensamblador x86-84 escrito en V), el propio V, además de muchos otros.

### Debuggers ###
- Actualmente no ofrece un debugger. Sin embargo, está la opción de [V-Analyzer](https://github.com/v-analyzer/v-analyzer).

### Package Managers ###
- V ofrece su propio package manager, vpm, escrito en V.

Para conocer todas las herramientas disponibles en y para V, se puede leer una lista más extensa [acá] (https://github.com/vlang/awesome-v)


**Pregunta I.b:**

```
v run rotar.v <w> <k>
```

**Pregunta I.c:**
```
v run matriz.v
```