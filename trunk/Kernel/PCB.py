__author__ = 'Pato'

class PCB:

    def __init__(self, mempos, pid):
        self.pid = pid
        ##self.programState = Ready() arranca en New()
        self.memoryPosition = mempos
        self.pc = 0
        self.is_eof = false

    def get_memoryPosition(self):
        return self.memoryPosition

    #POR AHORA NO CREE LOS STATES, PORQUE NO HAY DIFERENCIA ENTRE EL DISENIO QUE TENEMOS
    #Y LO QUE DEBERIAN HACER SUS ESTADOS