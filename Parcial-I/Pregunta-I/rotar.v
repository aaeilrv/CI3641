
import os

/*
Tiene un string y un entero n como parámetros de entrada.
Estos son no mutables puesto que V no permite parámetros
mutables para los tipos string e int.
*/
fn rotar(w string, k int) string {
	if k < 0 {
		return "integer must be positive."
	}

	// Se declaran las variables mutables
	mut word := w
	mut n := k 

	n = k % word.len

	// Se rota word
	temp := w[0..n]
    word = word[n..] + temp

	return word
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
	w := os.args[1]
	mut k := os.args[2].int()

	println(rotar(w, k))
}