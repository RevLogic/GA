# Experimental Gate class
# RevSim beta
# Author: Chris Rabl

class Gate:
    operation = None
    line_values = {}
    
    def __len__(self):
        return len(self.controls) + len(self.targets)

    def cost(self):
        if len(self) < 2:
            return len(self)

    def eval(self, lines):
        self.line_values = lines
        #self.validate() # ensure we are applying a valid gate
        return self.operation()
    
    def all_controls(self):
        return all([self.line_values[control] for control in self.controls])
        
    
class SingleTargetGate(Gate):
    controls = []
    target = ""

    def __init__(self, controls, target):
        self.target = target
        self.controls = controls[:]
        
    
class MultipleTargetGate(Gate):
    controls = []
    targets = []

    def __init__(self, controls, targets):
        self.targets = targets[:]
        self.controls = controls[:]

    def swap(self, a, b):
        a, b = b, a


class SameTargetGate(Gate):
    target = ""

    def __init__(self, target):
        self.target = target


class Toffoli(SingleTargetGate):
    def invert_target(self):
        self.line_values[self.target] = not(self.line_values[self.target])

    def operation(self):
        if self.all_controls():
            self.invert_target()
        return self.line_values


class Swap(MultipleTargetGate):
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError        
        self.swap(self.line_values[self.targets[0]], self.line_values[self.targets[1]])
        return self.line_values


class Fredkin(MultipleTargetGate):
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError
        if all_controls():
            self.swap(self.line_values[self.targets[0]], self.line_values[self.targets[1]])
        return self.line_values


class Inverter(SameTargetGate):
    def operation(self):
        self.line_values[self.target] = not(self.line_values[self.target])
        return self.line_values
