from gates import *
from lines import *

class Cascade:
    gate_list = []
    lines = None

    def __init__(self):
        

    def run(self):
        for gate in gate_list:
            self.lines = gate.eval(self.lines)
