from cascade import *
from perms import *

class TruthTable:
    def __init__(self, cascade):
        self.output_columns = {}
        self.input_columns = {}
        self.c = cascade
        self.num_rows = 2**self.c.logical_width()
        self.calculate()

    def __eq__(self, other):
        return self.columns == other.get_columns()

    def recalculate(self):
        self.input_columns = {}
        self.output_columns = {}
        self.calculate()

    def calculate(self):
        width = self.c.logical_width() # can be replaced with len(labels)
        labels = self.c.variable_line_labels()
        constant_lines = self.c.constant_line_values()

        perms = binary_iterator(width)
        for perm in perms:
            updated_lines = dict(zip(labels, perm))
            self.c.update_lines(updated_lines)

            run_result = self.c.run()
            for key in run_result:
                line_dict = updated_lines
                if key in constant_lines:
                    line_dict = constant_lines
                try:
                    self.input_columns[key].append(int(line_dict[key]))
                    self.output_columns[key].append(int(run_result[key]))
                except KeyError:
                    # Create a new column for a key we haven't seen yet
                    self.input_columns[key] = [ int(line_dict[key]) ]
                    self.output_columns[key] = [ int(run_result[key]) ]
                    
    def get_output_columns(self):
        return self.output_columns

    def get_input_columns(self):
        return self.input_columns

    def __str__(self):
        if(self.c.is_updated()):
            self.recalculate() # Fixes issue #10
        
        # TODO: clean this up because it's pretty atrocious at the moment -CR
        # also, make it look nicer, because right now printing makes it look like a pile of crap
        output_string = ""
        
        sorted_keys = [key for key in self.input_columns]
        sorted_keys.sort()
        
        passthrough = 0

        input_keys = ""
        output_keys = ""
        separator = "-" * (2*len(sorted_keys)+3)
        for key in sorted_keys:
            input_keys += key
            
        for key in sorted_keys:
            output_keys += key
            
        output_string += input_keys+" | "+output_keys + "\n"
        output_string += separator + "\n"
        
        for i in range(0, self.num_rows):
            output_row = ""
            in_str = ""
            for key in sorted_keys:
                in_str += str(self.input_columns[key][i])
            output_row += in_str
            output_row += " | "
            out_str = ""
            for key in sorted_keys:
                out_str += str(self.output_columns[key][i])
            output_row += out_str
            output_string += output_row + "\n"
            if(in_str == out_str):
                passthrough += 1

        summary = "\nPassthrough cases: " + str(passthrough*100.0/self.num_rows) + "%\n"
        output_string += summary
        return output_string
            
