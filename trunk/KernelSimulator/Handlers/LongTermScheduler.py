from Queue import PriorityQueue

__author__ = 'Pato'

class LongTermScheduler:

    def __init__(self):
        self.waiting_queue = PriorityQueue

    def handle_pcb(self, pcb,a_short_scheduler):

        self.waiting_queue.append(pcb)
        if a_short_scheduler.ready_queue.not_full:
            first_pcb = self.waiting_queue._get(self,self.waiting_queue) #quiero agarrar al primero
            #first_pcb.setState(new Ready()) #si la cola de waiting tiene lugar deberia pasar ahi
            #hacer el state con enum
            a_short_scheduler.push_to_queue(first_pcb)
