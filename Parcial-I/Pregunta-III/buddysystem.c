#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 50

struct Block {
    int start;
    int end;
    char name[MAX_LENGTH];
    struct Block* next;
};

struct Block* memory;

int is_power_of_two(int n) {
    if (n == 0) {
        printf("Debe reservar al menos un bloque de memoria.\n");
        exit(1);
    }

    return (n & (n - 1));
}

int which_power_of_two(int n) {
    if (n <= 0) {
        return -1; // No es una potencia de 2
    }
    int count = 0;
    while (n > 1) {
        if (n & 1) {
            return -1; // No es una potencia de 2
        }
        count++;
        n = n >> 1;
    }
    return count;
}

void initialize_memory(int total_blocks) {

    /* Si el número de bloques no es una
    potencia de 2, se obtiene la potencia
    de 2 más cercana.
    */
    while (is_power_of_two(total_blocks)) {
        total_blocks++;
    }

    int power_of_two = which_power_of_two(total_blocks);

    printf("power of two: %d\n", power_of_two);

    memory = (struct Block*)malloc(sizeof(struct Block));
    memory->start = 0;
    memory->end = total_blocks - 1;
    memory->next = NULL;
}

void reserve_memory(int size, char* name) {
    struct Block* current = memory;
    struct Block* previous = NULL;

    while (current != NULL) {
        int available_size = current->end - current->start + 1;

        if (available_size >= size) {
            if (current->next == NULL || current->next->start - current->end - 1 >= size) {
                struct Block* new_block = (struct Block*)malloc(sizeof(struct Block));
                new_block->start = current->end - size + 1;
                new_block->end = current->end;
                strcpy(new_block->name, name);
                new_block->next = current->next;
                current->end -= size;

                if (current->next != NULL) {
                    current->next->start -= size;
                }

                current->next = new_block;
                return;
            }
        }

        previous = current;
        current = current->next;
    }

    printf("No hay suficiente espacio libre para reservar %d bloques para %s.\n", size, name);
}

void release_memory(char* name) {
    // Implementar la liberación de memoria
}

void show_memory() {
    // Implementar la visualización de la memoria
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Por favor, proporcione la cantidad de bloques de memoria como argumento.\n");
        return 1;
    }

    int total_blocks = atoi(argv[1]);
    initialize_memory(total_blocks);

    char action[10], name[MAX_LENGTH];
    int size;

    while (1) {
        printf("Ingresa una acción (RESERVAR, LIBERAR, MOSTRAR, SALIR): ");
        scanf("%s", action);

        if (!strcmp(action, "RESERVAR")) {
            scanf("%d %s", &size, name);
            reserve_memory(size, name);
        } else if (!strcmp(action, "LIBERAR")) {
            scanf("%s", name);
            release_memory(name);
        } else if (!strcmp(action, "MOSTRAR")) {
            show_memory();
        } else if (!strcmp(action, "SALIR")) {
            break;
        } else {
            printf("Acción no reconocida. Inténtalo de nuevo.\n");
        }
    }

    return 0;
}
