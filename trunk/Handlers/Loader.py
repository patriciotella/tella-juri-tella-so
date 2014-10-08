__author__ = 'Pato'

class Loader:

    def __init__(self):

        super(Loader, self).__init__()

    def run(self,a_command,a_hard_disk,a_memory):

        program_on_disk = a_hard_disk.seek_program(command)
        memory_position = a_memory.write_program(program_on_disk)
        return memory_position