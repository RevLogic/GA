# Implementation of a Cube class to represent terms in an ESOP
# Author: Christopher Rabl - 001051542


# Truth table value enum used to define cubes
class TruthValue:
    false, true, dontcare = range(3)


# Basic "cube" class which allows us to specify a cube in the form:
# cube = Cube([x_1,x_2,...,x_n], [f_1,f_2,...,f_n])
# Cubes should always have the same number of inputs and outputs.
class Cube:
    cube_name = ""
    input_set = set()
    output_set = set()

    def __init__(self, input_list, output_list, name="Unnamed Cube"):
        self.cube_name = name
        # Cubes must have the same number of inputs as they have outputs
        if len(input_list) == len(output_list):
            self.input_set = set(input_list)
            self.output_set = set(output_list)
        else:
            self.cube_name = "INVALID CUBE"

    def count_inputs(self, val="all"):
        count = 0
        if val == "all":
            return len(self.input_set)
        for item in self.input_set:
            if item == val:
                count += 1
        return count

    def count_outputs(self, val="all"):
        count = 0
        if val == "all":
            return len(self.output_set)
        for item in self.output_set:
            if item == val:
                count += 1
        return count

    # Count output and inputs in common: need to implement same techniques as above
    def inputs_in_common(self, cube):
        return self.input_set.intersection(cube.input_set)

    def outputs_in_common(self, cube):
        return self.output_set.intersection(cube.output_set)

    def __repr__(self):
        return self.cube_name
