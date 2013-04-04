filename = open('/Users/rubinrana/Desktop/testFile.txt', 'r')
list = []
#add all the lines from file to a list
for line in filename:
	list.append( line )

#find string .begin and .end - get it's index value
startIndex = list.index('.begin\n')
endIndex = list.index('.end\n')

#loop throught the startIndex to endIndex and parse string
for i in range(startIndex+1, int(endIndex)):
	cascade = list[i].split() #split the string to a list
	firstString = cascade[0] #grab first string from the list i.e t3
	gateType = firstString[0] #first char to gate type
	numOfVar = firstString[1] #second char to num of inputs
	numOfVar = int(numOfVar) #convert string to int
	
	
	#Multiple Control Toffoli gates (MCT)
	if gateType == 't':
		print "c.append( Toffoli (",cascade[1:numOfVar+1],",s ) )"
	
	#Multiple Control Fredkin gate (MCF)
	elif gateType == 'f':
		print "c.append( Fredkin ( ",cascade[1:numOfVar+1],",s ) )"
	
	#Peres gate (P)
	elif gateType == 'p':
		print "Peres gate:"
		
	#implement swap and inverter. Locate example of gateType char in revlib
		
 
