import sys

def is_power_of_two(n):
    return (n & (n - 1) == 0) and n != 0

def get_power_of_two(n):
    if is_power_of_two(n):
        return n
    else:
        while not is_power_of_two(n):
            n += 1
    return n

class Node:
    def __init__(self, size, name, interval, parent, is_free=True):
        self.size = size
        self.name = name
        self.left = None
        self.right = None
        self.parent = parent

        self.start_interval = interval[0]
        self.end_interval = interval[1]

        self.is_free = is_free

class BuddySystem:
    reserved = []

    def __init__(self, total_memory):
        value = get_power_of_two(total_memory)
        self.root = Node(value, None, (0, value - 1), None)

    def add_process(self, size, name):
        if name in [i.name for i in self.reserved]:
            print(f"Error: El proceso {name} ya se encuentra reservado.")
        else:
            self.allocate_space(self.root, size, name)

    '''def allocate_space(self, node, size, name):
        if node.size == size and node.is_free:
            node.name = name
            node.is_free = False
            self.mark_parents_as_not_free(node.parent)
            self.reserved.append(node)
        elif node.size == size and not node.is_free:
            print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
        elif node.size > size:
            if (node.size // 2) < size: # Cuando un proceso no es potencia de 2
                node.name = name
                node.is_free = False
                self.reserved.append(node)         
            elif (node.size // 2) >= size and not node.left and not node.right: # Cuando un proceso no tiene hijos
                node.left = Node(node.size // 2, None, (node.start_interval, node.start_interval + (node.size//2) - 1), node)
                node.right = Node(node.size // 2, None, (node.start_interval + node.size//2, node.end_interval), node)
                self.allocate_space(node.left, size, name)
            elif (node.size // 2) >= size and node.left and node.right: # Cuando un proceso tiene hijos
                left_free = self.find_free_child(node.left, size)
                right_free = self.find_free_child(node.right, size)

                if left_free is not None: # Ver si hay espacio en el hijo izq. o sus hijos
                    self.allocate_space(node.left, size, name)
                elif right_free is not None: # Ver si hay espacio en el hijo izq. o sus hijos
                    self.allocate_space(node.right, size, name)
                else:
                    print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
        else:
            print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")'''
    
    def allocate_space(self, node, size, name):
        if node.size == size and node.is_free:
            node.name = name
            node.is_free = False
            self.mark_parents_as_not_free(node.parent)
            self.reserved.append(node)
        elif node.size == size and not node.is_free:
            print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
        elif node.size > size:
            # 1. Cuando un proceso no es potencia de 2
            if (node.size // 2) < size:
                node.name = name
                node.is_free = False
                self.reserved.append(node)
            # 2. Cuando un proceso es potencia de 2 y no tiene hijos
            elif (node.size // 2) >= size and not node.left and not node.right:
                # 2.1 Cuando el proceso que se está viendo es la raiz
                if node == self.root and not node.is_free:
                    print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
                    return
                node.left = Node(node.size // 2, None, (node.start_interval, node.start_interval + (node.size//2) - 1), node)
                node.right = Node(node.size // 2, None, (node.start_interval + node.size//2, node.end_interval), node)
                self.allocate_space(node.left, size, name)
            # 3. Cuando un proceso es potencia de 2 y tiene hijos
            elif (node.size // 2) >= size and node.left and node.right:
                left_free = self.find_free_child(node.left, size)
                right_free = self.find_free_child(node.right, size)

                # 3.1 Ver si hay espacio en el hijo izq. o sus hijos
                if left_free is not None:
                    self.allocate_space(node.left, size, name)
                # 3.2 Ver si hay espacio en el hijo izq. o sus hijos
                elif right_free is not None:
                    self.allocate_space(node.right, size, name)
                else:
                    print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
        else:
            print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")

    def deallocate_process(self, name):
        node = self.find_node(self.root, name)
        if node is None:
            print(f"El proceso {name} no existe o no tiene memoria reservada.")
        else:
            node.name = None
            node.is_free = True
            if node.parent.right.is_free:
                node.parent.left = None
                node.parent.right = None
                node.parent.is_free = True

    ### Auxiliar Functions ####

    def mark_parents_as_not_free(self, node):
        if node:
            node.is_free = False
            self.mark_parents_as_not_free(node.parent)

    def find_free_child(self, node, needed_space):
        if node:
            if node.is_free and node.size >= needed_space:
                return node.size
            else:
                result = self.find_free_child(node.left, needed_space)
                if not result:
                    result = self.find_free_child(node.right, needed_space)
                return result
        else:
            return None
        
    def find_node(self, node, name):
        if node:
            if node.name == name:
                return node
            else:
                result = self.find_node(node.left, name)
                if not result:
                    result = self.find_node(node.right, name)
                return result
        else:
            return None

    def print_not_reserved(self, node):
        if node:
            self.print_not_reserved(node.right)
            if node.is_free:
                print("(", node.start_interval,"->", node.end_interval,")")
            self.print_not_reserved(node.left)

    def print_reserved(self):
        for node in self.reserved:
            print(node.name, ":", "(", node.start_interval,"->", node.end_interval,")")

    def print_tree(self):
        print("\n")
        print("Memoria reservada:")
        self.print_reserved()
        print("\n")
        print("Memoria no reservada:")
        self.print_not_reserved(self.root)
        print("\n")



def main(arg1):

    total_blocks = int(arg1)
    buddy_system = BuddySystem(total_blocks)

    while True:
        action = input("Ingresa una acción (RESERVAR, LIBERAR, MOSTRAR, SALIR): ").split()
        if action[0].lower() == "reservar":
            if len(action) < 3:
                print("Error: faltó información.")
                continue
            size = int(action[1])
            name = action[2]
            buddy_system.add_process(size, name)

        elif action[0].lower() == "liberar":
            if len(action) < 2:
                print("Error: faltó información.")
                continue
            name = action[1]
            buddy_system.deallocate_process(name)

        elif action[0].lower() == "mostrar":
            buddy_system.print_tree()

        elif action[0].lower() == "salir":
            break
        else:
            print("Error: Acción inválida.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python3 buddysystem.py <cantidad de bloques de memoria a manejar>")
        sys.exit(1)
    arg1 = sys.argv[1]
    main(arg1)