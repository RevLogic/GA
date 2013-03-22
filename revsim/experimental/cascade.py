from gates import *
from lines import *
from truth_table import *

class Cascade:
    gate_list = []
    lines = None
    constant_lines = {}

    def __init__(self, lines, constants=[]):
        self.gate_list = []
        self.lines = lines.copy()
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

    # TODO: This method should probably live in the GeneticAlgorithm class since it's
    #       not really a Cascade method, but a computation that we do ON Cascades.
    def crossover(self, soulmate):
        c = Cascade(self.lines)
        print "len(self)/2 =", len(self)/2
        print "len(soulmate)/2 =", len(soulmate)/2
        for gate in self[0:len(self)/2]:
            c.append(gate)
        for gate in soulmate[len(soulmate)/2:len(soulmate)]:
            c.append(gate)
        return c
    
    # TODO: REMOVE THIS FUNCTIONALITY FROM THE CASCADE CLASS, these should be global functions...
    def truth_table(self):
        return TruthTable(self)

    def check_function(self, garbage_lines, target_truth_table):
        pass
    # END TODO

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
