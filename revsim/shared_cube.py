"""
Given a Cascade, output its cube-list and a new Cascade which
has the same function, but has been reduced using the method
of Nayeem-Rice.

Note that in order to generate the shared-cube representation
of a Cascade, it is required that Cascades have designated
"output lines" that are initialized to 0. These lines may be 
targets and controls to gates. Any line that is NOT an output
line MUST NOT BE USED AS A TARGET.
"""
from revsim import *

class SharedCube:
    def __init__(self, cascade):
        self.c = cascade
        self.output_lines =  cascade.constant_line_labels() # change this

    def generate(self):
        # this code is horrible
        cube_list = {}

        for gate in self.c: 
            target = gate.get_target()
            if target in self.output_lines:
                controls = tuple(gate.get_controls())
                try:
                    cube_list[controls].append(target)
                except KeyError:
                    cube_list[controls] = [target]
                        
        # select all cubes shared by a given key
        shared_key_values = {}
        for key in cube_list:
            if key[0] in self.output_lines:
                shared_key_values[key] = cube_list[key]
        
        for item in shared_key_values:
            shared_key = item[0]
            shared_value = shared_key_values[item]
            for key in cube_list:
                if shared_key in cube_list[key]:
                    cube_list[key] += shared_value
            del cube_list[item]

        for key in cube_list:
            print key, sorted(cube_list[key])
