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

fn (mut n Nodo) insertar_random(val f64) {
	// Se utiliza un número aleatorio para
	// decidir si se inserta a la izquierda o a la derecha
	if rand.int() % 2 == 0 {
		if n.existe_izq() {
			n.izq.insertar_random(val)
		} else {
			n.izq = &Nodo{val, 0, 0, n.nivel + 1}
		}
	} else {
		if n.existe_der() {
			n.der.insertar_random(val)
		} else {
			n.der = &Nodo{val, 0, 0, n.nivel + 1}
		}
	}
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
	/*
	Utiliza valores aleatorios que a la vez ingresan a una hoja
	aleatoria al árbol, por lo que puede o no ser un max heap (y
	ser simétrico).
	*/
	mut arbol_no_max_heap := Nodo{100, 0, 0, 0}
	for i := 0; i < 10; i++ {
		arbol_no_max_heap.insertar_random(rand.int())
	}

	imprimir_por_niveles(mut arbol_no_max_heap)

	print(": ")

	if arbol_no_max_heap.es_max_heap() {
		arbol_no_max_heap.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	// Segundo Arbol
	/*
	Al ingresar siempre el mismo valor, tanto el recorrido en preorder
	como postorder serán iguales, por lo que resultará en un max heap
	simétrico.
	*/
	mut arbol_max_heap := Nodo{100, 0, 0, 0}
	for i := 0; i < 10; i++ {
		arbol_max_heap.insertar_random(100)
	}

	imprimir_por_niveles(mut arbol_max_heap)

	print(": ")

	if arbol_max_heap.es_max_heap() {
		arbol_max_heap.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	println("\n")

	// Tercer Arbol
	/*
	En este caso, dado que que la raíz es 100 y los valores ingresados
	son menores a 100, siempre va a resultar en un árbol binario de
	búsqueda que a la vez es max-heap. Queda ver si es simétrico.

	Si se cambiara el valor inicial por uno menor a 100 o se quitara la
	condición de que los hijos de este deben ser siempre menores a él, no
	sería un max heap.
	*/
	mut arbol_binary_tree_search := Nodo{100, 0, 0, 0}
	for i := 0; i < 10; i++ {
		arbol_binary_tree_search.insertar_binary_tree_search(rand.int() % 100)
	}

	imprimir_por_niveles(mut arbol_binary_tree_search)

	print(": ")

	if arbol_binary_tree_search.es_max_heap() {
		arbol_binary_tree_search.es_max_heap_simetrico()
	} else {
		println("No es un max heap.")
	}

	// Cuarto Árbol
	/*
	Se ingresan valores conocidos en un orden ya creado justo para cumplir
	la condición de max-heap simétrico. Se hace la aserción de que lo sea.
	*/
}
