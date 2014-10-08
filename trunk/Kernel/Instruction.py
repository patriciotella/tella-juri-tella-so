__author__ = 'Pato'

class Instruction:

    ##TIENE QUE DECIR EL TIPO DE INSTRUCCION QUE ES, SI ES PARA UN DISPOSITIVO I/O O PARA EL CPU
    ## SI ES DE I/O TIENE QUE DECIR EL DISPOSITIVO AL QUE TIENE QUE IR

    def __init__(self, instruction, a_console):
        self.what_to_do = instruction
        self.myconsole = a_console

    def execute(self):
        self.myconsole.printInConsole(self.get_what_to_do())

    def get_what_to_do(self):
        return self.what_to_do