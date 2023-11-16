struct Cero {}

struct Succ {
	prev Church
}

type Church = Cero | Succ

fn cero() Church {
	return Cero{}
}

fn succ(prev Church) Church {
	return Succ{prev}
}

fn num_church(n int) Church {
	if n == 0 {
		return cero()
	} else {
		return succ(num_church(n - 1))
	}
}

fn (n Church) suma_church(m Church) Church {
	match n {
		Cero { return m }
		Succ { return succ(n.prev.suma_church(m)) }
	}
}

fn (n Church) multiplicacion_church(m Church) Church {
	match n {
		Cero { return cero() }
		Succ { return m.suma_church(n.prev.multiplicacion_church(m)) }
	}
}

fn (c Church) str() string {
	return match c {
		Cero { 'Cero' }
		Succ {'Suc(${c.prev})'}
	}
}

fn main() {
	church_cero := num_church(0)
	church_uno := num_church(1)
	church_dos := num_church(2)

	println("\nNúmeros de church:")

	println("0: ${church_cero.str()}") // 'Cero'
	println("1: ${church_uno.str()}")  // 'Suc(Cero)'
	println("2: ${church_dos.str()}")  // 'Suc(Suc(Cero))'

	println("\nSuma de números de church:")

	suma_uno := church_uno.suma_church(church_cero)
	suma_dos := church_uno.suma_church(church_dos)
	suma_tres := church_dos.suma_church(church_uno)
	suma_cuatro := num_church(3).suma_church(num_church(4))

	println("1 + 0: ${suma_uno.str()}") // 'Suc(Cero)'
	println("1 + 2: ${suma_dos.str()}") // 'Suc(Suc(Suc(Cero)))'
	println("2 + 1: ${suma_tres.str()}") // 'Suc(Suc(Suc(Cero)))'
	println("3 + 4: ${suma_cuatro.str()}") // 'Suc(Suc(Suc(Suc(Cero))))'

	println("\nMultiplicación de números de church:")
	
	mult_uno := church_uno.multiplicacion_church(church_cero)
	mult_dos := church_dos.multiplicacion_church(num_church(3))
	mult_tres := num_church(5).multiplicacion_church(num_church(4))

	println("1 * 0: ${mult_uno.str()}") // 'Cero'
	println("2 * 3: ${mult_dos.str()}") // 'Suc(Suc(Suc(Suc(Suc(Suc(Cero))))))'
	println("5 * 4: ${mult_tres.str()}") // 'Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Cero))))))))))))))))))))'

	println("\n")
}