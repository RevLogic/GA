from cascade import *
from gates import *

class RealWriter:
    def __init__(self, c):
        self.c = c
        self.lines = c.lines
        self.constant_lines = c.constant_line_labels()
        self.variables_lines = c.variable_line_labels()

    def write(self, file_name):
        f = open(file_name, 'w')
        variable_list = sorted(self.lines.keys())
        num_vars = str(len(variable_list))
        constant_list = []
        for variable in variable_list:
            if variable in self.constant_lines:
                constant_list.append(str(self.lines[variable]))
            else:
                constant_list.append("-")

class RealReader:
    def __init__(self, file_name):
        self.circuit_file = file_name
        pass

    def read_cascade(self):
        try:
            filename = open(self.circuit_file, 'r') #change this to cmd argv 
            myList = [] #to store all the lines from file
            tempConstants = [] #temp var to hold constant values
            
            #add all the lines from file to a list
            for line in filename:
                myList.append( line )
                if '.variables' in line: #find the variables line
                    variables = line
                if '.inputs' in line: #find .input line
                    inputs = line
	       	if '.outputs' in line: #find .output line
                    outputs = line
	       	if '.constants' in line: #find .constant line
                    constants = line
	       	if '.garbage' in line: #find .garbage line
                    garbage = line
		
            lineDict = {} #create an empty dictionary to store set of usable lines for our circuit

            variables = variables.split() #put the variables line in list
            variables.pop(0) #remove word .variable from list
            numOfVars = len(variables) #get number of variables

            inputs = inputs.split() #put input line in a list
            inputs.pop(0) #remove word .input from list

            outputs = outputs.split() #put .output line in a list
            outputs.pop(0) #remove word .output from list

            constants = constants.split() #put .constants line in a list
            constants.pop(0) #remove word .constants from list
            constants = list(constants[0])
            
            garbage = garbage.split() #put .garbage line in a list
            garbage.pop(0) #remove word .garbage from list
            garbage = list(garbage[0])
	
            #keep only valid constant variables
            for j in range(numOfVars):
                if constants[j] == '0':
                    tempConstants.append(variables[j])
	
            constants = tempConstants
	
            for x in range(numOfVars): #add variables to dictionary with initial value of 0
                if inputs[x] == '1' :
                    lineDict[variables[x]] = 1
                else:
                    lineDict[variables[x]] = 0	

            #print 'lines :', lineDict
            #print 'Variables :',variables
            #print 'Constants : ',constants 
            #print 'Garbage : ',garbage
       	    #print 'Inputs : ',inputs
            #print 'Outputs : ',outputs
	
            #find string .begin and .end - get it's index value
            startIndex = myList.index('.begin\n')
            endIndex = myList.index('.end\n')

            if len(constants) !=0:
                c = Cascade( lineDict, constants)
            else:
                c = Cascade (lineDict)
                
            #loop throught the startIndex to endIndex and parse string
            for i in range(startIndex+1, int(endIndex)):
                myCascade = myList[i].split() #split the string to a list
                firstString = myCascade[0] #grab first string from the list i.e t3
                gateType = firstString[0] #first char to gate type
                numOfInput = firstString[1] #second char to num of inputs
                numOfInput = int(numOfInput) #convert string to int
	
                #Single Control Toffoli gates (MCT)
                #a single "target" line label - picked the last from variable list to be a
                # target 
                if gateType == 't':
                    c.append( Toffoli (myCascade[1:numOfInput],myCascade[-1] ) )
                        
                #Multiple Control Fredkin gate (MCF)
                #Two "target" line label - picked last two from variable list to be target
                elif gateType == 'f':
                    c.append( Fredkin ( myCascade[1:numOfInput-1],variables[-2:]) )

                #implement swap and inverter. Locate example of gateType char in revlib
		
            #print "Quantum Cost:", c.cost()	
            #print "Number of Gates:", len(c)
            #print "Number of Lines:", c.width()
            #print "Number of Variable Lines:", c.logical_width()

            non_garbage_outputs = []
            garbage_dict = dict(zip(variables, garbage))
            for key in garbage_dict:
                if garbage_dict[key] != "1":
                    non_garbage_outputs.append(key)
		
            return c, non_garbage_outputs
            #t = TruthTable(c)
            #print t
	
	except LookupError as e:
	    print e
	except IOError as e:
            print e

