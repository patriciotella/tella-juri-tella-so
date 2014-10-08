from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.PCB import PCB
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput

__author__ = 'Pato'

class Cpu_model:

    def __init__(self, memo, quan):
        self.memory = memo
        self.quantum = quan

    def execute(self, pcb):
        count = self.quantum
        while count > 0 :
            #try:
                if self.memory.get_instruction_of_cell(pcb.memoryPosition) == 'EOF':
                    #setP¿State con enum
                    print('termino el proceso')
                    break
                else:
                    self.memory.get_instruction_of_cell(pcb.memoryPosition).execute
                    count -= 1
                    pcb.memoryPosition += 1
            #except ValueError:
            #    print('termino el proceso')
            #    break

            #count -= 1
        return new PcbHandler(self.pcb)



my_console = ConsoleOutput()
my_program = Program('QueNombreTePongo')
my_instruction = Instruction('open solitaire', my_console)
my_instruction2 = Instruction('cry because you dont have friends', my_console)
my_program.add_instruction(my_instruction)
my_program.add_instruction(my_instruction2)
pcb = PCB(0, 'a')
memory = Memory()
memory.write_program(my_program)
my_cpu = Cpu_model(memory, 20)

if __name__ == '__main__':
    my_cpu.execute(pcb)