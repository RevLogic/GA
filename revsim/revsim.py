"""
RevSim - A Reversible Logic Simulator
Christopher Rabl, Rio Lowry, Rubin Rana
"""

from perms import *

import copy
import sys
import operator
import pickle
import json


def arg(n):
    """
    Helper function to get variables from sys.argv[].
    """
    return int(sys.argv[n])

def swap(target1, target2):
    """
    Defines an uncontrolled SWAP gate, which is analogous to
    crossing wires in a classical logic design.
    
    target1: First target to swap, will become the second target
    target2: Second target to swap, will become the first target
    
    Returns: A list with the targets swapped
    """
    return (target2, target1)

def toffoli(controls, target):    
    """
    Defines a Toffoli gate given a list of inputs.
    
    controls: list of control line indices
    target: the target index within the list of inputs
    
    new_target: the new value of the target function
    
    DOES NOT CHANGE THE VALUE OF THE CONTROL FUNCTIONS
    NOTE: The list of controls MUST NOT contain the target.
    """
    return operator.xor(target, all(controls))

def inverter(controls, target):    
    """
    Defines an inverter based on a single control (CNOT).
    
    controls: list of control line indices (must contain exactly one control)
    target: ignored, assumed to be the control
    """
    if(len(controls) != 1):
        print "Warning: A control bit is being ignored!"
    return operator.not_(controls[0]) # We do this because in an inverter, there is ONLY one control

def fredkin(controls, targets):        
    """
    Defines a multiple-control Fredkin (CSWAP) gate.
    
    controls: list of control line indices
    targets: list of target line indices (must contain exactly two targets)
    
    If input lines are all 1, then swap the target lines, otherwise do nothing
    targets: updated list of targets
    """
    if(all(controls)):
        targets[0], targets[1] = targets[1], targets[0]
    return targets

def apply(lines, f, controls, target):
    """
    Apply an arbitrary function to a list of lines according to a list of controls and a target.
    
    lines: list of lines
    f: a function (e.g.: tof, inv)
    controls: list of controls to send to function f
    target: single target to send to function f
    
    out: list of line states after the function has been performed
    """
    out = lines[:] # We must make a COPY of the list of lines... see issue #1

    if f == swap:
        out[controls], out[target] = f(lines[controls], lines[target])
        return out
    try:
        out[target[0]], out[target[1]] = f([lines[i] for i in controls], [lines[target[0]], lines[target[1]]])
    except(TypeError):
        out[target] = f([lines[i] for i in controls], lines[target])
    return out

class Cascade:
    """
    Defines a cascade of gates which perform operations on a list of lines.
    
    >>> lines = [...] # list of lines and their initial states
    >>> c = Cascade(lines)
    >>> print c.run() # output the final state of the cascade
    """
    def __init__(self, lines, file_name=""):
        self.lines = lines[:]
        self.gates = []
        self.controls = []
        self.targets = []
        self.cost = 0
        if file_name:
            if file_name[-4:] == "json":
                self.load_json(file_name)
            else:
                self.read_pickle(file_name)

    def __iter__(self):
        """
        Given 3 lists of gates, controls, and targets, the zip function groups them into tuples
        which each contain a gate, the control list, and the target associated with that gate.
        gates := [tof, tof, fred]
        controls := [[0,1], [1,2], [0,2]]
        targets := [2, 0, [0,2]]
        zip(gates, controls, targets) = [(tof, [0,1], 2), (tof, [1,2], 0), (fred, [0,2], [0,2])]
        """
        for gate, control, target in zip(self.gates, self.controls, self.targets):
            yield (gate.func_name, control, target)


    def __getitem__(self, key):
        return (self.gates[key].func_name, self.controls[key], self.targets[key])


    def __setitem__(self, key, value):
        if len(value) != 3:
            raise TypeError
        self.gates[key] = value[0]
        self.controls[key] = value[1]
        self.targets[key] = value[2]


    def __len__(self):
        return len(self.gates) # Without loss of generality...

    def copy(self):
        """
        Factory method for creating a copy of the current object
        """
        return copy.deepcopy(self)
    
    # TODO: Define other built-ins such as __lt__ (less than) which allows us to compare
    # Cascades based on quantum cost, etc. Can be VERY useful in our GA!
    
    def insert(self, op, control, target, pos):
        """
        Insert a function, control-list, and target into the current Cascade's
        gate-list, control-list, and target-list
        """
        if pos > len(self) or pos < 0:
            raise ValueError
        
        self.gates.insert(pos, op)
        self.controls.insert(pos, control)
        self.targets.insert(pos, target)
        # Jackie's method: count ALL inputs, not just controls; opposed to Maslov
        self.cost += self.calculate_quantum_cost(op, len(control) + 1, 0)

    def append(self, op, control, target):
        """
        Append the current function, control list, and target to the
        gate-list, control-list, and target-list.
        NOTE: This does NOT evaluate the function on the list
        """
        self.insert(op, control, target, len(self))

    def prepend(self, op, control, target):
        """
        Prepend the current function, control list, and target to the
        gate-list, control-list, and target-list.
        NOTE: As with append, this does NOT evaluate the Cascade on the list
        """
        self.insert(op, control, target, 0)

    def remove(self, pos):
        """
        Delete the gate, controls, and targets at the specified index from the
        gate-list, control-list, and target-list.
        """
        if pos < 0:
            raise IndexError
        del self.gates[pos]
        del self.controls[pos]
        del self.targets[pos]

    def run(self, debug=False):
        """
        Output the result of running the input line values through
        the current cascade. May be called with c.run(True) to output
        intermediate line states.
        """
        output_lines = self.lines[:]
        for i in range(len(self.gates)):
            # Apply the current function to all lines in the cascade
            output_lines = apply(output_lines, self.gates[i], self.controls[i], self.targets[i])
            if debug:
                print output_lines # Debugging only, call c.run(True) to see intermediate steps
        # Python quirk: we want to display all outputs as integers
        output_lines = [int(line) for line in output_lines]
        return output_lines

    def replace_lines(self, lines):
        """
        Allows the user to replace the lines in the current circuit and re-run
        the cascade on the new line values.
        """
        self.lines = lines[:] # Need to copy the values, see issue #1

    def calculate_quantum_cost(self, op, size, garbage):
        """
        Quantum cost calculation using the table provided by the quantum wizard Maslov:
        http://webhome.cs.uvic.ca/~dmaslov/definitions.html
        """
        itemCost = 0
        

        toffoliCost = {(size, 0): 2**size - 3,
                       (size, 1): 24*size - 88,
                       (size, size-3): 12*size - 34}
        
        if size == 0:
            return itemCost
        elif size == 1:
            itemCost = 1
        elif size > 1 and 0 <= garbage <= 1:
            itemCost = toffoliCost[(size, garbage)]
        elif size > 1 and garbage == size - 3:
            itemCost = toffoliCost[(size, size-3)]
        else:
            itemCost = 1

        if op == fredkin:
            itemCost += 2
        elif op == inverter:
            itemCost = 1

        return itemCost

    def quantum_cost(self):
        return self.cost

    def fitness_vector(self):
        return len(self), self.cost

    def width(self):
        return len(self.lines)

    def write_pickle(self, file_name):
        """
        Serializes the current Cascade's state into a file which may be loaded in at a later time.
        """
        f = open(file_name, "w")
        pickle.dump([self.lines, self.gates, self.controls, self.targets, self.cost], f)
        f.close()

    def read_pickle(self, file_name):
        """
        Replaces the Cascade's current state with the state read from a file.
        Right now it uses the pickle module to do this, but a better choice might be JSON.
        """
        f = open(file_name)
        self.lines, self.gates, self.controls, self.targets, self.cost = pickle.load(f)
        f.close()

    def write_json(self, file_name):
        """
        Doesn't work just yet...
        """
        json_encoded = open(file_name, "w")
        json_encoded = json.dumps([self.lines, self.gates, self.controls, self.targets, self.cost])
        json_encoded.close()

    def read_json(self, file_name):
        """
        Ditto.
        """
        json_encoded = open(file_name)
        self.lines, self.gates, self.controls, self.targets, self.cost = json.load(json_encoded)
        json_encoded.close()

    def permutation_matrix(self):
        if self.width() > 10:
            raise ValueError
        
        # Create an empty (sparse) matrix
        matrix = [[0 for i in range(2**self.width())] for j in range(2**self.width())]

        # Fill the matrix by encoding the lines of the truth table
        for perm in binary_iterator(self.width()):
            lines = perm
            self.replace_lines(lines)
            out_lines = self.run()
            # INSERT MAGIC AND HAND-WAVING
            row_index = int("".join([str(i) for i in lines]), 2)
            column_index = int("".join([str(j) for j in out_lines]), 2)
            matrix[row_index][column_index] = 1

        for row in matrix:
            print " ".join([str(entry) for entry in row]) # Pretty print the matrix

    def truth_table(self):
        for perm in binary_iterator(self.width()):
            lines = perm
            self.replace_lines(perm)
            out_lines = self.run()
            print lines, out_lines
