from cascade import *
from perms import *

class TruthTable:
    output_columns = {}
    input_columns = {}
    c = None
    num_rows = 0

    def __init__(self, cascade):
        self.c = cascade
        self.calculate()

    def __eq__(self, other):
        return self.columns == other.get_columns()

    def calculate(self):
        width = self.c.logical_width() # can be replaced with len(labels)
        labels = self.c.variable_line_labels()
        self.num_rows = 2**width
        
        perms = binary_iterator(width)
        for perm in perms:
            updated_lines = dict(zip(labels, perm))
            self.c.update_lines(updated_lines)

            run_result = self.c.run()
            for key in run_result:
                try:
                    self.input_columns[key].append(updated_lines[key])
                    self.output_columns[key].append(int(run_result[key]))
                except KeyError:
                    self.input_columns[key] = [ updated_lines[key] ]
                    self.output_columns[key] = [ int(run_result[key]) ]
                    
    def get_columns(self):
        return self.output_columns

    def get_input_columns(self):
        return self.input_columns

    def __str__(self):
        output_string = ""
        
        sorted_keys = [key for key in self.input_columns]
        sorted_keys.sort()
        
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
            for key in sorted_keys:
                output_row += str(self.input_columns[key][i])
            output_row += " | "
            for key in sorted_keys:
                output_row += str(self.output_columns[key][i])
            output_string += output_row + "\n"

        return output_string
            
