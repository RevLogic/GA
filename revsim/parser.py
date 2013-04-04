filename = open('testFile.txt', 'r')
list = []
#add all the lines from file to a list
for line in filename:
	list.append( line )
	if '.variables' in line: #find the variables line
		variables = line

variables = variables.split() #put the variables line in list
variables.pop(0) # remove phrase .variable from list
numOfVars = len(variables) #get number of variables
lineDict = {} #create an empty dictionary to store set of usable lines for our circuit

for x in range(numOfVars): #add variables to dictionary with initial value of 0
	lineDict[variables[x]] = 0
	
print 'lines :', lineDict

#find string .begin and .end - get it's index value
startIndex = list.index('.begin\n')
endIndex = list.index('.end\n')



#loop throught the startIndex to endIndex and parse string
for i in range(startIndex+1, int(endIndex)):
	cascade = list[i].split() #split the string to a list
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
		
 
