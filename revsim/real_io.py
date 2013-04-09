from cascade import *
from gates import *

class RealWriter:
    def __init__(self, c):
        self.c = c
        self.variables = c.lines
        self.lines = c.lines
        self.constant_lines = c.constant_line_labels()
        self.variables_lines = c.variable_line_labels()
