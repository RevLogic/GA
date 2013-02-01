# RevSim - A Reversible Logic Simulator
# Christopher Rabl, Rio Lowry, Rubin Rana

import sys
import operator

# Helper function to get variables from sys.argv
def arg(n):
    return int(sys.argv[n])


# Defines a Toffoli gate given a list of inputs
#
# Input:
#     controls := list of control line indices
#     target := the target index within the list of inputs
#
# Outputs:
#    new_target := the new value of the target function
#    DOES NOT CHANGE THE VALUE OF THE CONTROL FUNCTIONS
#
# NOTE: The list of controls MUST NOT contain the target.
#
def tof(controls, target):
    return operator.xor(target, all(controls))


# Defines an inverter based on a single control
#
# Input:
#    controls := list of control line indices (must contain exactly one control)
#    target := ignored, assumed to be the control
#
# Output:
#    not(control[0])
#
def inv(controls, target):
    if(len(controls) != 1):
        print "Warning: A control bit is being ignored!"
    return operator.not_(controls[0]) # We do this because in an inverter, there is ONLY one control

# Apply an arbitrary function to a list of lines according to a list of controls and a target
#
# Input:
#    lines := list of lines
#    f := a function (e.g.: tof, inv)
#    controls := list of controls to send to function f
#    target := single target to send to function f
#
# Output:
#    out := list of line states after the function has been performed
#
def apply(lines, f, controls, target):
    out = lines
    out[target] = f([lines[i] for i in controls], lines[target])
    return out

# Defines a cascade of gates which perform operations on a list of lines
#
# Usage:
#    lines = [...] # list of lines and their initial states
#    c = Cascade(lines)
#    print c.run() # output the final state of the cascade
#
class Cascade:
    def __init__(self, lines):
        self.lines = lines
        self.gates = []
        self.controls = []
        self.targets = []

    # Append the current function, control list, and target to the
    # gate-list, control-list, and target-list
    # NOTE: This does NOT evaluate the function on the list
    #
    def append(self, op, control, target):
        self.gates.append(op)
        self.controls.append(control)
        self.targets.append(target)

    # Output the result of running the input line values through
    # the current cascade. May be called with c.run(True) to output
    # intermediate line states
    #
    def run(self, debug=False):
        for i in range(len(self.gates)):
            # Apply the current function to all lines in the cascade
            self.lines = apply(self.lines, self.gates[i], self.controls[i], self.targets[i])
            if debug:
                print self.lines # Debugging only, call c.run(True) to see intermediate steps

        # Python quirk: we want to display all outputs as integers
        self.lines = [int(line) for line in self.lines]

        return self.lines
