#!/usr/bin/env/python
# Revsim: a reversible logic framework
# C. Rabl, R. Lowry, H. Rana

import random
import sys

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
    print "Revsim - Milestone 5 (Release Master)"
    print "C. Rabl, R. Lowry, H. Rana"
    print ""
    filename = sys.argv[2]
    if sys.argv[1] == "--split":
        split_ga(filename)
    else:
        ga_runner(filename)
