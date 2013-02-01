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

def apply(lines, f, controls, target):
    out = lines
    out[target] = f(filter(lambda x: lines.index(x) in controls, lines), lines[target])
    return out
