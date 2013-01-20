#!/usr/bin/python

# Implementation of the sub-list generation algorithm described in [Nayeem2004]
# Algorithm by: N. M. Nayeem and J. E. Rice
# Implemented by: Christopher Rabl - 001051542


from cube import *

        
# Selects the cube from the cube_list with the largest number of 1's in
# its output specification. (Generation of sub-lists, step 3)
def largest_shared_cubes(cubes):
    largest = 0
    largest_cube = Cube([],[])
    
    for cube in cubes:
        if(cube.count_outputs() > largest):
            largest = cube.count_outputs()
            largest_cube = cube

    return largest_cube


# Select any cubes that have exactly the same output list as the current_cube
# (Generation of sub-lists, step 3, move all of them to sub_list_k)
def identical_cubes(cubes, current_cube):
    new_cube_list = []
    current_sub_list = []
    
    for cube in cubes:
        if cube.outputs_in_common(current_cube) == current_cube.output_set:
            current_sub_list.append(cube)
        else:
            new_cube_list.append(cube)
    
    return new_cube_list, current_sub_list


# Filter cube_list into two separate lists based on terms which do not share any
# outputs with any other terms (ungrouped_list), and all others (cube_list)
def filter_ungrouped_cubes(cubes):
    new_cube_list = []
    new_ungrouped_list = []

    for i in cubes:
        no_shared_outputs = 1
        for j in cubes:
            if (i != j) and (len(i.outputs_in_common(j)) == 0):
                no_shared_outputs += 1

        if(no_shared_outputs == len(cubes)):
            new_ungrouped_list.append(i)
        else:
            new_cube_list.append(i)

    return new_cube_list, new_ungrouped_list


# Select cubes which share all of the cubes in sub_list[k]
# (Generation of sub-lists, step 4)
def shared_cubes(cube_list, sub_list):
    new_cube_list = cube_list
    new_sub_list = sub_list
    # Change the above to new_cube_list = [] ... etc.
    
    return new_cube_list, new_sub_list


def main():
    
    test_cube_list = [ Cube(['x1','x2','x3'], ['f1','f2','f3'], 'A'), 
                       Cube(['x1','x3','x4'], ['f1','f4','f5'], 'B'),
                       Cube(['x1','x7','x8'], ['f1','f2','f3'], 'C'),
                       Cube(['x2','x3','x4','x5'], ['f3','f4','f5','f2'], 'D'),
                       Cube(['x6'], ['f6'], 'E'), Cube(['x7', 'x8'], ['f8','f7'], 'F') ]
    
    cube_list = test_cube_list
    ungrouped_list = []
    sub_list = []
    
    current_cube = Cube([],[])
    k = 0

    cube_list, ungrouped_list = filter_ungrouped_cubes(cube_list)

    while cube_list:
        current_cube = largest_shared_cubes(cube_list)
        sub_list.append([]) # Create a new sub-list
        cube_list, sub_list[k] = identical_cubes(cube_list, current_cube)
        cube_list, sub_list[k] = shared_cubes(cube_list, sub_list[k])

        print "k:", k
        print "current_cube:", current_cube
        print "cube_list:", cube_list
        print "ungrouped_list:", ungrouped_list
        print "sub_list:", sub_list
        print ""

        k += 1
