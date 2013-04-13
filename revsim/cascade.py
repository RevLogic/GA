# Cascade class
# Author: Christopher Rabl

from gates import *
import copy
import pickle

class Cascade:
    def __init__(self, lines, constants=[]):
        """
        Cascade constructor which initializes an empty Cascade with lines
        """
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
        """
        Returns the number of gates in a given Cascade.
        c = Cascade(...)
        ...
        len(c) # Returns the number of gates in c
        """
        return len(self.gate_list)
    
    def __eq__(self, other):
        # TODO: Implement
        if len(self) != len(other):
            return False

        # We can't just compare gate-lists because
        # two of the same gates will be different instances
        # of the class
        for i in range(0, len(self)):
            if self[i] != other[i]:
                return False


        if self.lines != other.lines:
            return False
        
        if self.constant_lines != other.constant_lines:
            return False

        return True
    
    def remove(self, pos):
        """                                                                     
        Delete the gate, controls, and targets at the specified index from the  
        gate-list, control-list, and target-list.                               
        """
        if pos < 0 or pos >= len(self) or len(self) == 0:
            raise IndexError
        del self.gate_list[pos]
        self.updated = True

    def run(self):
        """
        Evaluate the result of all gates in the Cascade according to specific line values.
        """
        self.updated = False
        for gate in self.gate_list:
            gate.eval(self.lines)
        return self.lines

    def update_lines(self, lines):
        # This function is now called update_lines because it doesn't
        # really "replace" them in the conventional set. The values are
        # still there, but we can change any ones we want

        for line in lines:
            if line not in self.lines:
                raise ValueError
        
        # Merge current line set with existing line set
        self.lines.update(lines)

        # Make sure the constant lines stay constant
        self.lines.update(self.constant_lines)
        self.updated = True

    def replace_gates(self, gates):
        # TODO: Test for replacement validity
        self.gate_list = gates
        
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
        """
        Calculates the quantum cost of the Cascade by running through the entire
        gate list and keeping a tally of each gate's cost.
        """
        quantum_cost = 0
        for gate in self.gate_list:
            quantum_cost += gate.cost()
        return quantum_cost

    def width(self):
        """
        Returns the number of lines in the Cascade
        """
        return len(self.lines)

    def logical_width(self):
        """
        Returns the number of variable lines (non-constant lines) in the Cascade
        """
        return len(self.lines) - len(self.constant_lines)
    
    def variable_line_labels(self):
        variable_lines = []
        for key in self.lines:
            if key not in self.constant_lines:
                variable_lines.append(key)
        variable_lines.sort()
        return variable_lines

    def constant_line_labels(self):
        constant_lines = []
        for key in self.constant_lines:
            constant_lines.append(key)
        constant_lines.sort()
        return constant_lines

    def constant_line_values(self):
        return self.constant_lines

    def is_updated(self):
        return self.updated

    def reset_updated(self):
        self.updated = False

    def copy(self):
        """
        Returns a deep copy of the current Cascade. "Must go deeper." -JZ
        """
        return copy.deepcopy(self)

    def write_pickle(self, file_name):
        """
        Serializes the current Cascade's state into a file which may be loaded in at a later time.
        c = Cascade(...)
        c.append(...)
        ...
        c.write_pickle("file_name.pckl")
        """
        f = open(file_name, "w")
        pickle.dump([self.lines, self.gate_list, self.constant_lines, self.updated], f)
        f.close()

    def read_pickle(self, file_name):
        """
        Replaces the Cascade's current state with the state read from a file.
        Right now it uses the pickle module to do this, but a better choice might be JSON.

        c = Cascade({}) # Create an empty Cascade with no lines
        c.read_pickle("file_name.pckl")
        """
        f = open(file_name)
        self.lines, self.gate_list, self.constant_lines, self.updated = pickle.load(f)
        f.close()
        
