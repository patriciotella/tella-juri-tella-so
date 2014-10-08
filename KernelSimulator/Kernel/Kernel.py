__author__ = 'Pato'

class Kernel:

    def __init__(self, a_memory, a_disk,a_long_scheduler, a_short_scheduler, a_loader):
        self.pcb_instruction =[]
        self.my_memory = a_memory
        self.my_hard_disk = a_disk
        self.pid = 1
        self.my_long_scheduler = a_long_scheduler
        self.my_short_scheduler = a_short_scheduler
        self.my_loader = a_loader

    def run(self, command):

        memory_position = self.my_loader.run(command,self.my_hard_disk,self.my_memory)
        self.create_pcb(memory_position, self.pid)



    def create_pcb(self, memory_position):
        pcb = PCB(memory_position, self.pid)
        self.pcb_instruction.append(pcb) #ESTA AL PEDO, HABRIA QUE BORRARLO
        self.my_long_scheduler.handle_pcb(pcb,self.my_short_scheduler)
        self.pid +=1
        # return pc

    #def send_to_queue(self, pcb):
     #   self._my_scheduler.send_to_queue(pcb)