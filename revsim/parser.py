import sys
try:
	filename = open(sys.argv[1], 'r') #change this to cmd argv 
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

	print 'Variables :',variables
	print 'Inputs : ',inputs
	print 'Outputs : ',outputs
	print 'Constants : ',constants 
	print 'Garbage : ',garbage
	
	for x in range(numOfVars): #add variables to dictionary with initial value of 0
		if inputs[x] == '1':
			lineDict[variables[x]] = 1
		else:
			lineDict[variables[x]] = 0	
	
	print 'lines :', lineDict

	#find string .begin and .end - get it's index value
	startIndex = myList.index('.begin\n')
	endIndex = myList.index('.end\n')



	#loop throught the startIndex to endIndex and parse string
	for i in range(startIndex+1, int(endIndex)):
		cascade = myList[i].split() #split the string to a list
		firstString = cascade[0] #grab first string from the list i.e t3
		gateType = firstString[0] #first char to gate type
		numOfInput = firstString[1] #second char to num of inputs
		numOfInput = int(numOfInput) #convert string to int
	
	
		#Multiple Control Toffoli gates (MCT)
		if gateType == 't':
			print "c.append( Toffoli (",cascade[1:numOfInput+1],",s ) )"
	
		#Multiple Control Fredkin gate (MCF)
		elif gateType == 'f':
			print "c.append( Fredkin ( ",cascade[1:numOfInput+1],",s ) )"
	
		#Peres gate (P)
		elif gateType == 'p':
			print "Peres gate:"
		
		#implement swap and inverter. Locate example of gateType char in revlib

except LookupError as e:
    print e
except IOError as e:
	print e
		
 
