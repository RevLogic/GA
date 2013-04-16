#!/usr/bin/env python
# Revsim: a reversible logic framework
# C. Rabl, R. Lowry, H. Rana

import random
import sys
import os

from cascade import *
from gates import *
from truth_table import *
from shared_cube import *
from genetic import *
from naive_ga import *
from smart_ga import *
from real_io import *
from split_ga import *
from ga_runner import *

if __name__ == "__main__":
    try:
        print "Revsim - Milestone 5 (Release Master)"
        print "C. Rabl, R. Lowry, H. Rana"
        print ""
        if sys.argv[1] == "--split":
            filename = sys.argv[2]
            result = split_ga(filename)
        elif sys.argv[1] == "--quantum":
            filename = sys.argv[2]
            optimization_factor = float(sys.argv[3])
            result = ga_runner(filename, optimization_factor)
            for gate in result:
                print gate
        else:
            print "Usage:"
            print "--split <filename> : runs splitting GA on the cascade with no quantum cost optimization factor (recommended for large circuits)"
            print "--quantum <filename> <optimization factor %>: performs quantum cost optimization using the SmartGA method (recommended for small circuits)"
            print "--help : displays this help message"
    except KeyboardInterrupt:
        print "Stopped all Revsim subprocesses"
    except IndexError:
        print "For help, type ./revsim.py --help"
