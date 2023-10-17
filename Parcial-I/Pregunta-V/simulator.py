class Language:
    def __init__(self, name):
        self.name = name

class Program:
    def __init__(self, name):
        self.name = name
        self.language = []

    def add_language(self, language):
        self.language.append(language)

class Interpreter:
    def __init__(self, written_in, for_language):
        self.written_in = written_in
        self.for_language = for_language

class Translator:
    def __init__(self, written_in, source_language, target_language):
        self.written_in = written_in
        self.source_language = source_language
        self.target_language = target_language

class Simulator:
    def __init__(self):
        self.languages = []
        self.programs = {}
        self.interpreters = []
        self.translators = []
        
        self.languages.append(Language("LOCAL"))

    def define_language(self, name):
        self.languages.append(Language(name))

    def define_program(self, name, language):
        if name not in self.programs:
            self.programs[name] = Program(name)
            self.programs[name].add_language(language)
            print(f"Se definió el programa '{name}', ejecutable en '{language}'.")  
        else:
            if language not in self.programs[name].language:
                self.programs[name].add_language(language)
                print(f"Se definió el programa '{name}', ejecutable en '{language}'.")
            else:
                print(f"Error: El programa {name} ya está definido en el lenguaje {language}.")
    
    def define_interpreter(self, written_in, for_language):
        self.interpreters.append(Interpreter(written_in, for_language))
        print(f"Se definió un intérprete para {for_language} escrito en {written_in}.")
    
    def define_translator(self, written_in, source_language, target_language):
        self.translators.append(Translator(written_in, source_language, target_language))
        print(f"Se definió un traductor de  {source_language} hacia {target_language} escrito en {written_in}.")

    def is_executable(self, program_name):
        if program_name not in self.programs:
            print(f"Error: El programa '{program_name}' no se encuentra definido.")
            return False

        program = self.programs[program_name]
        for language in program.language:
            if language in [i.name for i in self.languages]:
                return True
            else:
                return False

    # Funciones auxiliares de impresión
    def print_programs(self):
        for program_name, program in self.programs.items():
            languages = ', '.join(program.language)
            print(f"Programa: '{program_name}', escrito en: {languages}")

    def print_languages(self):
        for language in self.languages:
            print(f"Lenguajes entendidos por la máquina: '{language.name}'")

    def print_translators(self):
        for translator in self.translators:
            print(f"Traductor de '{translator.source_language}' a '{translator.target_language}' escrito en '{translator.written_in}' ")

    def print_interpreters(self):
        for interpreter in self.interpreters:
            print(f"Intérprete de '{interpreter.for_language}' escrito en '{interpreter.written_in}' ")

def main():
    simulator = Simulator()

    while True:
        action = input("Ingresa una acción (DEFINIR, EJECUTABLE, SALIR): ").split()
        if action[0] == "DEFINIR":
            if action[1] == "PROGRAMA":
                if len(action) < 4:
                    print("Error: faltó información.")
                    continue

                name = action[2]
                language = action[3]
                simulator.define_program(name, language)

            elif action[1] == "INTERPRETE":
                if len(action) < 4:
                    print("Error: faltó información.")
                    continue

                written_in = action[2]
                for_language = action[3]

                # Se agrega un intérprete al simulador
                simulator.define_interpreter(written_in, for_language)
                
                # Si la máquina entiende el lenguaje written_in:
                if written_in in [i.name for i in simulator.languages] and for_language not in [i.name for i in simulator.languages]:
                    # 1. Ahora también entiende for_language
                    simulator.languages.append(Language(for_language))

                    # 2. La máquina entiende todos los lenguajes
                    # que tienen interprete escrito en for_language
                    interpreters_to_process = [for_language]
                    while interpreters_to_process:
                        current_interpreter = interpreters_to_process.pop(0)

                        for interpreter in simulator.interpreters:
                            if interpreter.written_in == current_interpreter:
                                if interpreter.for_language not in [i.name for i in simulator.languages]:
                                    simulator.languages.append(Language(interpreter.for_language))
                                interpreters_to_process.append(interpreter.for_language)

                    # 3. Si tengo un traductor de A a B escrito en C, la máquina entiende B y for_language = C,
                    # entonces tengo un traductor de A a B escrito en for_language
                    for existing_translator in simulator.translators:
                        if existing_translator.written_in == for_language and existing_translator.target_language in [i.name for i in simulator.languages]:
                            if existing_translator.written_in != existing_translator.target_language:
                                simulator.translators.append(Translator(written_in, existing_translator.source_language, existing_translator.target_language))

                        # 4. Si tengo un traductor de A a B escrito en C, la máquina entiende C
                        # y for_language = B, entonces la máquina entiende A
                        if existing_translator.written_in in [i.name for i in simulator.languages] and existing_translator.target_language == for_language:
                            if existing_translator.source_language not in [i.name for i in simulator.languages]:
                                simulator.languages.append(Language(existing_translator.source_language))

                        # 5. Si tengo un traductor de A a B escrito en C, con C = written_in,
                        # ahora tengo un traductor de A a B escrito en D, con D = for_language.
                        if existing_translator.written_in == written_in:
                            simulator.translators.append(Translator(for_language, existing_translator.source_language, existing_translator.target_language))

            elif action[1] == "TRADUCTOR":
                if len(action) < 5:
                    print("Error: faltó información.")
                    continue

                written_in = action[2]
                source_language = action[3]
                target_language = action[4]

                # Se agrega un traductor
                simulator.define_translator(written_in, source_language, target_language)

                # Si la máquina entiende written_in y target_language:
                if written_in in [i.name for i in simulator.languages] and target_language in [i.name for i in simulator.languages]:
                    if source_language not in [i.name for i in simulator.languages]:
                        # 1. Ahora entiende source_language
                        simulator.languages.append(Language(source_language))

                        # 2. Si tengo un traductor de X a source_language escrito en Y y la máquina entiende Y,
                        # entonces la máquina entiende X
                        for existing_translator in simulator.translators:
                            if existing_translator.written_in in [i.name for i in simulator.languages] and existing_translator.target_language == source_language:
                                if existing_translator.source_language not in [i.name for i in simulator.languages]:
                                    simulator.languages.append(Language(existing_translator.source_language))

                        # 3. Si yo tengo un traductor de X a Y escrito en source_language y la máquina entiende Y,
                        # entonces la máquina entiende X
                        for existing_translator in simulator.translators:
                            if existing_translator.written_in == source_language and target_language in [i.name for i in simulator.languages]:
                                simulator.languages.append(Language(existing_translator.source_language))                         
            else:
                print("Error: comando inválido.")
        
        elif action[0] == "EJECUTABLE":
            if len(action) != 2:
                print("Error: faltó información.")
                continue
            program_name = action[1]
            if simulator.is_executable(program_name):
                print(f"Si, es posible ejecutar el programa '{program_name}'.")
            else:
                print(f"No es posible ejecutar el programa '{program_name}'.")

        elif action[0] == "SALIR":
            break
        else:
            print("Error: Acción Inválida.")

if __name__ == "__main__":
    main()