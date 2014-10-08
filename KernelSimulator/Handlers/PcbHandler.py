__author__ = 'Pato'

class PcbHandler:
    
    def __init__(self,a_kernel a_pcb):
        
        super(PcbHandler, self).__init__()

        if(a_pcb.is_oef == false):
            self.a_kernel.my_short_scheduler.push_to_queue(a_pcb)