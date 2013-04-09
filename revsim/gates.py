# Revsim gate class
# Author: Chris Rabl

class Gate:
    """
    Abstract base class to define basic gate behavior
    """
    def __init__(self):
        self.line_values = {}
    
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
    """
    Base class to define behavior of gates with multiple controls and only one target
    All SingleTargetGates use lists to define their controls and a string literal to define the target
    """
    def __init__(self, controls, target):
        if target in controls:
            raise ValueError
        self.target = target
        self.controls = controls[:]

    def __len__(self):
        return len(self.controls) + 1

    def __eq__(self, other):
        # Check if the instances are of the same subclass
        if isinstance(self, other.__class__):
            if (self.target == other.target) and (self.controls == other.controls):
                return True
        return False
    
    def get_controls(self):
        return sorted(self.controls)

    def get_target(self):
        return self.target

    
class MultipleTargetGate(Gate):
    """
    Base class to define the behavior of gates with multiple controls and multiple targets
    All MultipleTargetGates use lists to define their controls and targets
    """
    def __init__(self, controls, targets):
        self.targets = targets[:]
        self.controls = controls[:]

    def __eq__(self, other):
        # Check if the instances are of the same subclass
        if isinstance(self, other.__class__):
            if (self.targets == other.targets) and (self.controls == other.controls):
                return True
        return False

    def swap(self, a, b):
        val_a = self.targets[a]
        val_b = self.targets[b]
        self.line_values[val_b], self.line_values[val_a] = self.line_values[val_a], self.line_values[val_b]
        

class SameTargetGate(Gate):
    """
    Base class to define the behavior of gates with only one target and no controls (that are the same line)
    All SameTargetGates use only a single string to define the target, controls are not supported
    """
    def __init__(self, target):
        self.target = target

    def __len__(self):
        return 1

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            if self.target == other.target:
                return True
        return False

    def get_target(self):
        return self.target

    def get_controls(self):
        return [self.target]

class Toffoli(SingleTargetGate):
    """
    Defines the behavior of a Toffoli gate when applied to the lines in a Cascade
    """
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

    def __str__(self):
        out = "t"
        out += str(len(self)) + " "
        for control in self.controls:
            out += control + " "
        out += self.target
        return out

class Swap(MultipleTargetGate):
    """
    Defines the behavior of an uncontrolled Swap gate
    """
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError        
        self.swap(0, 1)
        return self.line_values


class Fredkin(MultipleTargetGate):
    """
    Defines the behavior of a controlled swap gate (Fredkin gate)
    """
    def operation(self):
        if len(self.targets) != 2:
            raise ValueError
        if self.all_controls():
            self.swap(0, 1)
        return self.line_values
    
    def __str__(self):
        out = "f"
        out += str(len(self))
        out += " "
        for control in self.controls:
            out += control + " "
        for target in self.targets:
            out += target + " "
        return out

class Inverter(SameTargetGate):
    """
    Defines the behavior of a simple inverter acting on a line.
    In the .real file format, this is referred to as a Toffoli gate which only
    has one input (the target).
    """
    def operation(self):
        self.line_values[self.target] = not(self.line_values[self.target])
        return self.line_values

    def __str__(self):
        out = "t1 "
        out += self.target
        return out
