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

            if language not in self.programs[name].language:
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

        program = self.programs[program_name]
        for language in program.language:
            if language in [i.name for i in self.languages]:
                return True
            else:
                return False

    # Funciones auxiliares para imprimir los programas, lenguajes y traductores

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
        
def main():
    simulator = Simulator()

    while True:
        action = input("Ingresa una acción (DEFINIR, EJECUTABLE, SALIR): ").split()
        if len(action) >= 4 and action[0] == "DEFINIR":
            if action[1] == "PROGRAMA":
                name = action[2]
                language = action[3]
                simulator.define_program(name, language)

                # Si existe un intérprete hacia A escrito en language, se agrega A como lenguaje del programa
                for existing_interpreter in simulator.interpreters:
                    if existing_interpreter.for_language == language:
                        simulator.programs[name].add_language(existing_interpreter.written_in)

                # Si existe un traductor desde language hacia A, se agrega A como lenguaje del programa
                for existing_translator in simulator.translators:
                    if existing_translator.source_language == language and existing_translator.written_in in [i.name for i in simulator.languages]:
                        simulator.programs[name].add_language(existing_translator.target_language)

                simulator.print_programs()

            elif action[1] == "INTERPRETE":
                written_in = action[2]
                for_language = action[3]

                # Se agrega un intérprete al simulador
                simulator.define_interpreter(written_in, for_language)

                # 1. si la máquina entiende el lenguaje written_in, ahora también entiende for_language
                if written_in in [i.name for i in simulator.languages] and for_language not in [i.name for i in simulator.languages]:
                    simulator.languages.append(Language(for_language))

                    # así también, ahora la máquina entiende todos los lenguajes
                    # que tienen interprete escrito en for_language
                    interpreters_to_process = [for_language]

                    while interpreters_to_process:
                        current_interpreter = interpreters_to_process.pop(0)

                        for interpreter in simulator.interpreters:
                            if interpreter.written_in == current_interpreter:
                                simulator.languages.append(Language(interpreter.for_language))
                                interpreters_to_process.append(interpreter.for_language)

                #2. Los programas escritos en written_in, ahora son ejecutables en for_language  
                for program in simulator.programs.values():
                    if written_in in program.language:
                        program.add_language(for_language)

                        # el programa también se puede correr en todos los lenguajes que
                        # tienen interpretador de for_language a otro lenguage
                        languages_to_add = [for_language]
                        while languages_to_add:
                            current_language = languages_to_add.pop(0)

                            for interpreter in simulator.interpreters:
                                if interpreter.written_in == current_language:
                                    program.add_language(interpreter.for_language)
                                    languages_to_add.append(interpreter.for_language)

                # 3. Si tengo un traductor escrito en written_in, ahora tengo uno escrito en for_language
                for existing_translator in simulator.translators:
                    if existing_translator.written_in == written_in:
                        simulator.translators.append(Translator(for_language, existing_translator.source_language, existing_translator.target_language))

                #simulator.print_programs()
                #simulator.print_languages()
                #simulator.print_translators()

            elif action[1] == "TRADUCTOR":
                written_in = action[2]
                source_language = action[3]
                target_language = action[4]

                # Se agrega un traductor
                simulator.define_translator(written_in, source_language, target_language)

                '''
                Para los programas en la máquina:
                si written_in lo entiende la máquina,
                y si un programa está escrito en source_language, entonces se puede
                traducir ese programa a target_language
                '''
                if written_in in [i.name for i in simulator.languages]:
                    for program in simulator.programs.values():
                        if source_language in program.language:
                            program.add_language(target_language)

                                # TO DO: si se agrega un traductor de B a C, y posteriormente uno de A a B,
                                # Los programas escritor en A ahora son ejecutables en C.

                '''
                Si tengo un traductor de A a B escrito en C
                y un traductor de de C a D escrito en E,
                ahora tengo u traductor de A a B escrito en D
                SOLO si la máquina entiende E
                '''
                for existing_translator in simulator.translators:
                    if existing_translator.written_in in [i.name for i in simulator.languages]:
                        if existing_translator.source_language == written_in:
                            simulator.translators.append(Translator(existing_translator.target_language, source_language, target_language))
                    #if existing_translator.written_in in [i.name for i in simulator.languages]:
                    #    simulator.translators.append(Translator(existing_translator.source_language, source_language, target_language))               
                
                #simulator.print_programs()
                #simulator.print_languages()
                simulator.print_translators()            
                
            else:
                print("Error: comando inválido.")
        
        elif action[0] == "EJECUTABLE":
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