from Handlers.ShortTermScheduler import ShortTermScheduler

__author__ = 'Pato'


class SC_priority(ShortTermScheduler):
    def __init__(self, cpu):

        super(self, cpu).__init__
        self.ready_queue = range(50)

    def push_to_queue(self, pcb):

        self.ready_queue = self.priority_push(self, pcb)

    def send_next_to_cpu(self):

        self.cpu.run(self.ready_queue.get(self))

    def priority_push(self, pcb):
        result = range(50)
        for i in ready_queue:
            if i.get_priority() < pcb.get_priority():
                result.append(i)
            else:
                result.append(pcb)
                res_index = i.index()
                break

        #for i = self.res_index , i < 51, i += 1:
        #    result.append(ready_queue(i))

        return result
        # esto no corre ni en pedo, la idea es que recorra la cola comparando prioridades, cuando la prioridad es menor a la ingresada
        #se agrega, y el resto se copia tal cual