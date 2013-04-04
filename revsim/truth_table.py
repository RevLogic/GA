from cascade import *
from perms import *

class TruthTable:
    def __init__(self, cascade, calc_stats=False):
        self.output_columns = {}
        self.input_columns = {}
        self.c = cascade
        self.num_rows = 2**self.c.logical_width()
        self.calculate()
        self.calc_stats = calc_stats
    
    def __eq__(self, other):
        """
        Compares two TruthTables to determine if they are identical.
        """
        self.__update_if_required()
        return self.output_columns == other.get_output_columns()

    def compare_columns(self, other, col_list):
        """
        Compares the columns specified in col_list of two TruthTables. Returns True if their
        entries are the same, False otherwise.
        """
        self.__update_if_required()
        for col in col_list:
            if self.output_columns[col] != other.get_output_columns()[col]:
                return False
        return True

    def fuzzy_compare_columns(self, other, col_list):
        """
        Returns a float value between 0 and 1 based on the number of identical entries in
        the columns of the current TruthTable specified by col_list. This value is computed as:
        number_of_identical_entries / number_of_entries
        If two columns are exactly the same, this function will return 1.0
        """
        self.__update_if_required()
        same = 0
        length = 0
        for col in col_list:
            col1 = self.output_columns[col]
            col2 = other.get_output_columns()[col]
            length = len(col1)
            for i in xrange(0, length):
                same += int(col1[i] == col2[i])
        return (float(same) / float(length*len(col_list)))

    def recalculate(self):
        """
        Recalculates the TruthTable if the Cascade is changed, or under other circumstances.
        Typically, this does not need to be called by end-user applications or libraries.
        """
        self.input_columns = {}
        self.output_columns = {}
        self.calculate()

    def calculate(self):
        """
        Computes the entries of the TruthTable by running every input permutation through
        the current TruthTable's cascade and recording the result. For Cascades with a large
        logical width, this computation is VERY expensive. This takes O(2^n) time in all cases.
        """
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
        self.__update_if_required()
        return self.output_columns

    def get_input_columns(self):
        self.__update_if_required()
        return self.input_columns

    def __update_if_required(self):
        if self.c.is_updated():
            self.recalculate()
            self.c.reset_updated()

    def __str__(self):
        """
        Allows the TruthTable to be printed or output to a file by constructing a string
        representation of it.
        """
        self.__update_if_required()
        
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
            if(self.calc_stats):
                if(in_str == out_str):
                    passthrough += 1

        if self.calc_stats:
            summary = "\nCASCADE STATISTICS\n\n"
            summary += "Passthrough cases: " + str(passthrough*100.0/self.num_rows) + "\n"
            output_string += summary
        return output_string
            
