# Implementation of a Cube class to represent terms in an ESOP
# Author: Christopher Rabl - 001051542

# Basic "cube" class which allows us to specify a cube in the form:
# cube = Cube([x_1,x_2,...,x_n], [f_1,f_2,...,f_n])
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

    def count_inputs(self):
        return len(self.input_set)

    def count_outputs(self):
        return len(self.output_set)

    def inputs_in_common(self, cube):
        return self.input_set.intersection(cube.input_set)

    def outputs_in_common(self, cube):
        return self.output_set.intersection(cube.output_set)

    def __repr__(self):
        return self.cube_name
