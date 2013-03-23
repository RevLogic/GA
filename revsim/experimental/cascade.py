# Experimental Cascade class
# RevSim beta
# Author: Christopher Rabl

from revsim import *

class Cascade:
    def __init__(self, lines, constants=[]):
        self.gate_list = []
        self.lines = lines.copy()
        self.constant_lines = {}
        self.updated = False
        for key in constants:
            self.constant_lines[key] = self.lines[key]

    def __getitem__(self, key):
        return self.gate_list[key]

    def __setitem__(self, key, value):
        self.gate_list[key] = value

    def __len__(self):
        return len(self.gate_list)
    
    def __eq__(self, cascade):
        # TODO: Implement
        return False
    
    def run(self):
        self.updated = False
        for gate in self.gate_list:
            gate.eval(self.lines)
        return self.lines

    def update_lines(self, lines):
        # This function is now called update_lines because it doesn't
        # really "replace" them in the conventional set. The values are
        # still there, but we can change any ones we want
        
        # Merge current line set with existing line set
        self.lines.update(lines)

        # Make sure the constant lines stay constant
        self.lines.update(self.constant_lines)
    
    def insert(self, gate, pos):
        """
        Insert a function, control-list, and target into the current Cascade's
        gate-list, control-list, and target-list
        """
        if pos > len(self) or pos < 0:
            raise ValueError

        self.gate_list.insert(pos, gate)
        self.updated = True

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

    def cost(self):
        quantum_cost = 0
        for gate in self.gate_list:
            quantum_cost += gate.cost()
        return quantum_cost

    def width(self):
        return len(self.lines)

    def logical_width(self):
        return len(self.lines) - len(self.constant_lines)
    
    def variable_line_labels(self):
        variable_lines = []
        for key in self.lines:
            if not(key in self.constant_lines):
                variable_lines.append(key)
        variable_lines.sort()
        return variable_lines

    def constant_line_values(self):
        return self.constant_lines

    def is_updated(self):
        return self.updated
