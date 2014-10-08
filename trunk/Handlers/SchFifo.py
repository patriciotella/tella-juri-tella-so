from Handlers.ShortTermScheduler import ShortTermScheduler

__author__ = 'Pato'

class SC_fifo (ShortTermScheduler):

    def _init__(self, cpu):
        super(self, cpu).__init__
        self.ready_queue = range(50)

    def push_to_queue(self, pcb):
        self.ready_queue.put(self,pcb)

    def send_next_to_cpu(self):
        self.cpu.run(self.ready_queue.get())