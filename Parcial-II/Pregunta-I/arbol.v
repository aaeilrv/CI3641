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

fn (mut n Nodo) insertar_binary_tree_search(val f64) {
	// Se inserta a la izquierda si es menor
	// y a la derecha si es mayor o igual
	if val < n.valor {
		if n.existe_izq() {
			n.izq.insertar_binary_tree_search(val)
		} else {
			n.izq = &Nodo{val, 0, 0, n.nivel + 1}
		}
	} else {
		if n.existe_der() {
			n.der.insertar_binary_tree_search(val)
		} else {
			n.der = &Nodo{val, 0, 0, n.nivel + 1}
		}
	}
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
	if nivel == 0 {
		print("   ${n.valor}")

	} else if nivel > 0 {
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
		println("existe izq")
		a.izq.post_order(mut nums)
	}

	if a.existe_der() {
		println("existe der")
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

	//post_order_nums = post_order_nums.reverse()

	if pre_order_nums == post_order_nums {
		println('Es max heap simetrico.')
		return true
	} else {
		println('No es max heap simetrico.')
		return false
	}
}

fn main() {

	/*
	Primer Árbol: max heap asimétrico
	*/
	mut tree_1 := Nodo{100,
		&Nodo{80, &Nodo{40, &Nodo{30, 0, 0, 3}, &Nodo{5, 0, 0, 3}, 2}, &Nodo{15, 0, 0, 2}, 1},
		&Nodo{80, &Nodo{15, 0, 0, 2}, &Nodo{40, &Nodo{5, 0, 0, 3}, &Nodo{30, 0, 0, 3}, 2}, 1}, 0}

	imprimir_por_niveles(mut tree_1)

	print(": ")

	if tree_1.es_max_heap() {
		tree_1.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	/*
	Segundo Árbol: max heap simétrico:
	El mismo valor en todas las hojas.
	*/
	mut tree_2 := Nodo{100,
		&Nodo{100, &Nodo{100, &Nodo{100, 0, 0, 3}, &Nodo{100, 0, 0, 3}, 2}, &Nodo{100, 0, 0, 2}, 1},
		&Nodo{100, &Nodo{100, 0, 0, 2}, &Nodo{100, &Nodo{100, 0, 0, 3}, &Nodo{100, 0, 0, 3}, 2}, 1}, 0}

	imprimir_por_niveles(mut tree_2)

	print(": ")

	if tree_2.es_max_heap() {
		tree_2.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	/*
	Tercer Árbol: Es simétrico porque sólo tiene
	un valor
	*/

	mut tree_3 := Nodo{100, 0, 0, 0}

	imprimir_por_niveles(mut tree_3)

	print(": ")

	if tree_3.es_max_heap() {
		tree_3.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	/*
	Cuarto Árbol: Asimétrico. Cada nodo sólo tiene hijos a la izquierda.
	*/

	mut tree_4 := Nodo{5, 0, &Nodo{4, 0, &Nodo{3, 0, &Nodo{2, 0, &Nodo{1, 0, 0, 4}, 3}, 2}, 1}, 0}

	imprimir_por_niveles(mut tree_4)

	print(": ")

	if tree_4.es_max_heap() {
		tree_4.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

}
