/*
Se verifica si una matriz es o no cuadrada
*/
fn check_square(matrix[][] int) bool {
	n := matrix.len

	for row in matrix {
		if row.len != n {
			return false
		}
	}

	return true
}

/*
Tiene como parámetro una matriz nxn.
Obtiene su matriz transpuesta.
*/
fn transpose(matrix[][] int) [][]int {
	if !check_square(matrix) {
		println('La matriz no es cuadrada.')
		exit(1)
	}

	n := matrix.len
	mut transposed := [][]int{len: n, init: []int{len: n}}
		
	for i in 0..n {
		for j in 0..n {
			transposed[i][j] = matrix[j][i]
		}
	}

	return transposed
}

/*
Tiene como parámetro dos matrices nxn.
Obtiene la multiplicación de ambas.
*/
fn matrix_mult(a[][] int, b[][] int) [][]int {
	if a.len != b[0].len {
		println('Las matrices no pueden ser multiplicadas.')
		exit(1)
	}

	n := a.len
	mut mult := [][]int{len: n, init: []int{len: n}}

	for i in 0..n {
		for j in 0..n {
			mult[i][j] = 0
			for k in 0..n {
				mult[i][j] += a[i][k] * b[k][j]
			}
		}
	}

	return mult
}


fn main() {

	matrix := [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	println(matrix_mult(matrix, transpose(matrix)))
}