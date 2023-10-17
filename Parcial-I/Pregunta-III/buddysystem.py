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
    def __init__(self, size, name, interval, parent, is_free=True, can_allocate=True):
        self.size = size
        self.name = name
        self.left = None
        self.right = None
        self.parent = parent

        self.start_interval = interval[0]
        self.end_interval = interval[1]

        self.is_free = is_free
        self.can_allocate = True

class BuddySystem:
    def __init__(self, total_memory):
        value = get_power_of_two(total_memory)
        self.root = Node(value, None, (0, value - 1), None)

    def add_process(self, size, name):
        self.allocate_space(self.root, size, name)

    def allocate_space(self, node, size, name):
        if node.is_free:
            if node.size == size:
                node.name = name
                node.is_free = False
                node.can_allocate = False
            elif node.size > size:
                if (node.size // 2) < size: # Cuando un proceso no es potencia de 2
                    node.name = name
                    node.can_allocate = False
                    node.is_free = False         
                if not node.left and not node.right and node.size // 2 >= size:
                    if node.size // 2 >= size:
                        node.left = Node(node.size // 2, None, (node.start_interval, node.start_interval + (node.size//2) - 1), node)
                        node.right = Node(node.size // 2, None, (node.start_interval + node.size//2, node.end_interval), node)
                        node.can_allocate = False
                        self.allocate_space(node.left, size, name)
                    else:
                        print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
                else:
                    if node.left and node.right:
                        self.allocate_space(node.right, size, name)
            else:
                print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")
        else:
            print(f"No hay suficiente memoria para el proceso {name} de tamaño {size}")

    def deallocate_process(self, name):
        node = self.find_node(self.root, name)
        if node is None:
            print(f"El proceso {name} no existe.")
        else:
            self.deallocate_space(self.root, node.name)

    def deallocate_space(self, node, name):
        print("to do")
        
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

    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.name, ":", "(", node.start_interval,"->", node.end_interval,")", node.can_allocate)
            self.print_tree(node.left, level + 1)

def main(arg1):

    total_blocks = int(arg1)
    buddy_system = BuddySystem(total_blocks)

    while True:
        action = input("Ingresa una acción (RESERVAR, LIBERAR, MOSTRAR, SALIR): ").split()
        if action[0] == "RESERVAR":
            if len(action) < 3:
                print("Error: faltó información.")
                continue
            size = int(action[1])
            name = action[2]
            buddy_system.add_process(size, name)

        elif action[0] == "LIBERAR":
            if len(action) < 2:
                print("Error: faltó información.")
                continue
            name = action[1]
            buddy_system.deallocate_process(name)

        elif action[0] == "MOSTRAR":
            buddy_system.print_tree(buddy_system.root)

        elif action[0] == "SALIR":
            break
        else:
            print("Error: Acción inválida.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python3 buddysystem.py <cantidad de bloques de memoria a manejar>")
        sys.exit(1)
    arg1 = sys.argv[1]
    main(arg1)