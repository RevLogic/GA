import operator

# Defines a Toffoli gate given a list of inputs
# Input:
#     controls := list of control lines
#     target := the target function within the list of inputs

# Outputs:
#    new_target := the new value of the target function
#    DOES NOT CHANGE THE VALUE OF THE CONTROL FUNCTIONS
# NOTE: The list of controls MUST NOT contain the target.
def tof(controls, target):
    return operator.xor(target, all(controls))

def inv(control, target):
    return operator.not_(control[0]) # We do this because in an inverter, there is ONLY one control

def apply(lines, f, controls, target):
    out = lines
    out[target] = f([lines[i] for i in controls], lines[target])
    return out

class Cascade:
    def __init__(self, lines):
        self.lines = lines
        self.gates = []
        self.controls = []
        self.targets = []

    def append(self, op, control, target):
        self.gates.append(op)
        self.controls.append(control)
        self.targets.append(target)
        
    def run(self, debug=False):
        for i in range(len(self.gates)):
            self.lines = apply(self.lines, self.gates[i], self.controls[i], self.targets[i])
            if debug:
                print self.lines
        return self.lines
