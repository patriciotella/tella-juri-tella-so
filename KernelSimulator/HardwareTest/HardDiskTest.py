from Kernel.Instruction import Instruction
from HardWare.HardDisk import HardDisk
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput
import unittest

__author__ = 'adri'


class HardwareTest(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk([self.program])

    def test_seek_program(self):
        program_founded = self.hdd.seek_program('testP')
        self.assertEqual(program_founded, self.program)

    def test_save_program(self):
        self.hdd.save_program(self.program)
        self.assertEqual(len(self.hdd.programs), 2)
