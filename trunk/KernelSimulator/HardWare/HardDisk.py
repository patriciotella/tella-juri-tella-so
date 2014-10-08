__author__ = 'Pato'


class Hard_disk:
    def __init__(self):
        self.programs = []

        def _init__(self, programs):
            self.programs = programs

        def seek_program(self, comand):
            for i in self.programs:
                print (i.get_program_name())
                if i.get_program_name() == comand:
                    return i
                # throw Program_not_found_exception

        def save_program(self, program):
            self.programs.append(program)

#TESTS BOLUDOS, GUARDAR Y BUSCAR UN PROGRAMA