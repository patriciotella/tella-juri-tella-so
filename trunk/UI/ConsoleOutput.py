__author__ = 'Pato'

class ConsoleOutput:

    def __init__(self):
        self.string_collection = []

    def printInConsole(self, data):
        self.string_collection.append(data)

    def get_collection(self):
        return self.string_collection