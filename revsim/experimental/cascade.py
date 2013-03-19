from gates import *
from lines import *

class Cascade:
    gate_list = []
    lines = None
    cost = 0

    def __init__(self, lines):
        self.lines = lines.copy()

    def __getitem__(self, key):
        return self.gate_list(key)

    def __len__(self):
        return len(self.gate_list)

    def run(self):
        for gate in self.gate_list:
            gate.eval(self.lines)
        return self.lines
    
    def insert(self, gate, pos):
        """
        Insert a function, control-list, and target into the current Cascade's
        gate-list, control-list, and target-list
        """
        if pos > len(self) or pos < 0:
            raise ValueError

        self.gate_list.insert(pos, gate)
        # self.cost += gate.quantum_cost() # TODO: make sure this works

    def append(self, gate):
        """
        Append the current function, control list, and target to the
        gate-list, control-list, and target-list.
        NOTE: This does NOT evaluate the function on the list
        """
        self.insert(gate, len(self))

    def prepend(self, gate):
        """
        Prepend the current function, control list, and target to the
        gate-list, control-list, and target-list.
        NOTE: As with append, this does NOT evaluate the Cascade on the list
        """
        self.insert(gate, 0)

