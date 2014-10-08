from Handlers.ShortTermScheduler import ShortTermScheduler

__author__ = 'Pato'

class SchRonRobin (ShortTermScheduler):

    def __init__(self,a_short_scheduler,a_cuantum):

        self.short_scheduler = a_short_scheduler
        self.cuantum = a_cuantum