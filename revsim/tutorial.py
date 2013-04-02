# Revsim tutorial


# Import the Revsim libraries
from revsim import *


# Declare a set of usable lines for our circuit
# We use a Python dictionary so that we can label our lines
lines = {'a':0, 'b':0, 'c':0, 's':0}
# Notice that we have given each "line" an initial value of 0:
# We may change this to be a 1 if that is what our circuit specifies


# We now declare a new Cascade. This structure will hold the gates in
# our circuit, and it will be used to create a truth table later on.
# The second parameter that we pass into our cascade defines the list of
# constant inputs (in this case, the 'c' and 's' lines should always
# start out as being 0 (or whatever their initial value in the "lines"
# dictionary were)
c = Cascade( lines, ['c', 's'] )


# Now, we can start adding gates to our circuit. We will be creating an
# adder in this example using three Toffoli gates. We can append them to
# our circuit, going from left to right. We append the gate using the
# Cascade.append(Gate) method

# Toffoli gates are a subclass of the SingleTargetGate class, so they expect
# a list of line labels to be used as "controls" (in this instance, ['a', 'b'])
# and a single "target" line label (in this case 'c').
c.append( Toffoli(['a', 'b'], 'c') )


# Now we can append two more gates to our cascade to complete our adder
# Notice that even though these Toffoli gates only have one control
# (these are called CNOT gates), the Toffoli class still expects us to pass in
# a LIST of controls.
c.append( Toffoli(['a'], 's') )
c.append( Toffoli(['b'], 's') )


# Another thing we can do is remove gates from any point in the circuit, we do
# this by calling Cascade.remove(pos) where pos is the index of the gate in the
# Cascade. Note that Cascades are zero-indexed:
c.remove(1) # Will remove Toffoli(['a'], 's')


# We can also insert gates at any point in our Cascade. Since we still want to
# create an adder, let's replace the gate that we just removed (insert at index 1):
c.insert( Toffoli(['a'], 's'), 1 ) 


# Once we have our circuit defined, we can do a lot of cool things with it.
# The first thing that we get for free with our Cascade class is quantum cost
# calculation. We can get the cost by doing:
print "Quantum Cost:", c.cost()
# Additionally, if we remove or insert gates from/into our Cascade, this cost
# is updated automatically, so all we need to do is call c.cost() to retrieve
# the new value.


# We can also count the number of gates in our circuit by using Python's
# built-in len() method:
print "Number of Gates:", len(c)


# We can count the number of lines by calling:
print "Number of Lines:", c.width()


# And finally, we can get the number of non-constant lines by calling:
print "Number of Variable Lines:", c.logical_width()


# Since Cascades are Python iterables, we can use them like lists and
# loop through them, outputting the gate instances from left to right.
# This will output the gate specification in the Revlib format:
for gate in c:
    print gate


