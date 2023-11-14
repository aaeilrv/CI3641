import rand

struct Nodo {
	valor f64
mut:
	izq  &Nodo = unsafe { nil }
	der  &Nodo = unsafe { nil }
	nivel int
}

fn (a Nodo) existe_izq() bool {
	return a.izq != unsafe { nil }
}

fn (a Nodo) existe_der() bool {
	return a.der != unsafe { nil }
}

fn (mut a Nodo) numero_de_hojas() int {
	mut pre_order_nums := []f64{}
	a.pre_order(mut pre_order_nums)
	return pre_order_nums.len
}

fn (mut n Nodo) insertar(val f64) {
	// Se utiliza un número aleatorio para
	// decidir si se inserta a la izquierda o a la derecha
	if rand.int() % 2 == 0 {
		if n.existe_izq() {
			n.izq.insertar(val)
		} else {
			n.izq = &Nodo{val, 0, 0, n.nivel + 1}
		}
	} else {
		if n.existe_der() {
			n.der.insertar(val)
		} else {
			n.der = &Nodo{val, 0, 0, n.nivel + 1}
		}
	}

	// En caso de que se quiera
	// crear un binary search tree
	/*if val < n.valor {
		if n.existe_izq() {
			n.izq.insertar(val)
		} else {
			n.izq = &Nodo{val, 0, 0, false}
		}
	} else {
		if n.existe_der() {
			n.der.insertar(val)
		} else {
			n.der = &Nodo{val, 0, 0, false}
		}
	}*/
}

fn imprimir_por_niveles(mut n Nodo) {
	nivel := n.numero_de_hojas()
	mut i := 0
	for i < nivel {
		imprimir_nivel_actual(n, i, 0)
		i++
	}
}

fn imprimir_nivel_actual(n Nodo, nivel f64, espacios int) {
	if nivel == 1 {
		print("   ${n.valor}")

	} else if nivel > 1 {
		if n.existe_izq() {
			imprimir_nivel_actual(n.izq, nivel - 1, espacios + 1)
		}
		if n.existe_der() {
			imprimir_nivel_actual(n.der, nivel - 1, espacios + 1)
		}
	}
}

fn (mut a Nodo) pre_order(mut nums []f64) {
	nums << a.valor

	if a.existe_izq() {
		a.izq.pre_order(mut nums)
	}

	if a.existe_der() {
		a.der.pre_order(mut nums)
	}
}

fn (mut a Nodo) post_order(mut nums []f64) {
	if a.existe_izq() {
		a.izq.post_order(mut nums)
	}

	if a.existe_der() {
		a.der.post_order(mut nums)
	}

	nums << a.valor
}

fn (mut a Nodo) es_max_heap() bool {
	if a.existe_izq() && a.existe_der() {
		if a.valor < a.izq.valor || a.valor < a.der.valor {
			return false
		} else {
			return a.izq.es_max_heap() && a.der.es_max_heap()
		}
	} else {
		return true
	}
}

fn (mut a Nodo) es_max_heap_simetrico() bool {
	mut pre_order_nums := []f64{}
	mut post_order_nums := []f64{}

	a.pre_order(mut pre_order_nums)
	a.post_order(mut post_order_nums)

	if pre_order_nums == post_order_nums {
		println('Es max heap simetrico.')
		return true
	} else {
		println('No es max heap simetrico.')
		return false
	}
}

fn main() {
	// Primer Arbol
	mut arbol_no_max_heap := Nodo{100, 0, 0, 0}
	arbol_no_max_heap.insertar(90)
	arbol_no_max_heap.insertar(80)
	arbol_no_max_heap.insertar(70)
	arbol_no_max_heap.insertar(60)
	arbol_no_max_heap.insertar(50)
	arbol_no_max_heap.insertar(40)
	arbol_no_max_heap.insertar(30)
	arbol_no_max_heap.insertar(20)
	arbol_no_max_heap.insertar(10)

	imprimir_por_niveles(mut arbol_no_max_heap)

	print(": ")

	if arbol_no_max_heap.es_max_heap() {
		arbol_no_max_heap.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	// Segundo Arbol
	mut arbol_max_heap := Nodo{100, 0, 0, 0}
	for i := 0; i < 10; i++ {
		arbol_max_heap.insertar(100)
	}
	imprimir_por_niveles(mut arbol_max_heap)

	print(": ")

	if arbol_max_heap.es_max_heap() {
		arbol_max_heap.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}
}
