# Implementation of a Cube class to represent terms in an ESOP
# Author: Christopher Rabl - 001051542


# Truth table value enum used to define cubes
class TruthValue:
    false, true, dontcare = range(3)


# Basic "cube" class which allows us to specify a cube in the form:

# cube = Cube([x_1,x_2,...,x_n], [f_1,f_2,...,f_n], name, width)
# [x_1,...,x_n] := input term list
# [f_1,...,f_n] := output term list
# name := basic name given to the cube, does not affect its input or outputs
# width := number of variables in the term

# Note: Cubes will always have the same number of inputs and outputs.
class Cube:
    cube_name = ""
    input_set = set()
    output_set = set()

    def __init__(self, input_list, output_list, name="Unnamed Cube", width=0):
        self.cube_name = name
        # Cubes must have the same number of inputs as they have outputs
        # and we must check that neither list length exceeds the width of the cube
        if len(input_list) == len(output_list) == width:
            self.input_set = set(input_list)
            self.output_set = set(output_list)
        else:
            self.cube_name = "INVALID CUBE"
            if len(input_list) != len(output_list):
                raise ValueError("Cube input list and output list must have the same length")
            else:
                raise ValueError("Length of input_list or output_list is different from cube width")

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
