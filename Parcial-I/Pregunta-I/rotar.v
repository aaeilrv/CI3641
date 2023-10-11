
import os

/*
Tiene un string y un entero n como parámetros de entrada.
Estos son no mutables puesto que V no permite parámetros
mutables para los tipos string e int.
*/
fn rotar(word string, spaces int) string {
	if spaces < 0 {
		return "integer must be positive."
	}

	// Se declaran las variables mutables
	mut rotated_word := word
	mut n := spaces 

	n = spaces % word.len

	// Se rota rotated_word
	temp := word[0..n]
    rotated_word = rotated_word[n..] + temp

	return rotated_word
}

fn main() {
	if os.args.len != 3 {
        println('How to use: v run rotar.v <word> <n>')
        return
    }

	/*
	Dado que V no acepta argumentos en main, se
	utiliza el slice os.args del módulo os para
	obtener los parámetros desde la línea de comandos.
	*/
	word := os.args[1]
	mut n := os.args[2].int()

	println(rotar(word, n))
}