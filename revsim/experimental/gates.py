# Experimental Gate class
# RevSim beta
# Author: Chris Rabl

class Gate:
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

    def operation(self):
        pass
    
class SingleTargetGate(Gate):
    controls = []
    target = ""

    def __init__(self, controls, target):
        self.target = target
        self.controls = controls[:]

    def __len__(self):
        return len(self.controls) + 1
    
class MultipleTargetGate(Gate):
    controls = []
    targets = []

    def __init__(self, controls, targets):
        self.targets = targets[:]
        self.controls = controls[:]

    def swap(self, a, b):
        self.line_values[self.targets[b]], self.line_values[self.targets[a]] = self.line_values[self.targets[a]], self.line_values[self.targets[b]]
        

class SameTargetGate(Gate):
    target = ""

    def __init__(self, target):
        self.target = target

    def __len__(self):
        return 1

class Toffoli(SingleTargetGate):
    def invert_target(self):
        self.line_values[self.target] = not(self.line_values[self.target])

    def operation(self):
        if self.all_controls():
            self.invert_target()
        return self.line_values

    def cost(self):
        size = len(self)

        garbage = 0 # TODO: is this right?
        toffoliCost = {(size, 0): 2**size - 3,
                       (size, 1): 24*size - 88,
                       (size, size-3): 12*size - 34}
        
        if size < 2:
            return size
        elif size == 3:
            return 5
        elif size > 1 and 0 <= garbage <= 1:
            return toffoliCost[(size, garbage)]
        elif size > 1 and garbage == size - 3:
            return toffoliCost[(size, size-3)]

        return 0

class Swap(MultipleTargetGate):
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError        
        self.swap(0, 1)
        return self.line_values


class Fredkin(MultipleTargetGate):
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError
        if self.all_controls():
            self.swap(0, 1)
        return self.line_values


class Inverter(SameTargetGate):
    def operation(self):
        self.line_values[self.target] = not(self.line_values[self.target])
        return self.line_values
