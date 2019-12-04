from pprint import pprint
def readInputFile():
	f = open("input.txt", "r")
	inputString = f.read()
	inputString = inputString.replace("\n","")
	inputString = inputString.strip()
	prgArr = inputString.split(",") # Original Array Data
	f.close()
	return prgArr

#for x in prgArr:
#	prgArr[x] = int(x)


#inputFileData = readInputFile()

prgArrInts = [int(a) for a in readInputFile()] # Converts everything to ints, nice
programArray = prgArrInts; # Data we can modify if we'd like

# programArray[1] = verb
# programArray[2] = noun


def checkIfOk(data):
	target = 19690720
	out = int(data[0])
	
	# "Smart" approach
	if target - out > 99:
		print("Too bad, missing " + str(target - out) + "!")
		return "more"
		
	elif target - out < 99:
		return target - out
		
	elif out > target:
		return "less"
		
	elif target == out:
		return "perfect"


def intcode(code): # Takes the program as an array of ints
	inputProg = ",".join(str(a) for a in code)
	#pprint(inputProg)
	intcode = code
	running = True
	pos = 0
	while running:
		#pprint("parsing position " + str(pos))
		op = intcode[pos]
		#print("OP="+str(op))
		#print("POS="+str(pos))
		if(op == 1):
			src1 = intcode[pos+1]
			src2 = intcode[pos+2]
			dst = intcode[pos+3]
			intcode[dst] = intcode[src1] + intcode[src2]
		elif(op == 2):
			src1 = intcode[pos+1]
			src2 = intcode[pos+2]
			dst = intcode[pos+3]
			intcode[dst] = intcode[src1] * intcode[src2]
		elif(op == 99):
			running = False
			break
		else:
			#print(op)
			#print(pos)
			raise UserWarning
		pos += 4

	return intcode
	#return ",".join([str(a) for a in intcode])

#pprint(intcode(programArray))
#print(prgArrInts)

#exit()

noun=0
nounF=0
verb=0
verbF=0
done = False
while done == False:
	
	programArray = [int(a) for a in readInputFile()] # Converts everything to ints, nice
	#pprint(",".join(str(a) for a in programArray))
	
	# Modify Input
	programArray[1] = noun
	programArray[2] = verb
	
	result = intcode(programArray)
	#print(",".join(str(a) for a in result))
	data = checkIfOk(result)
	print(data)
	if data == "more" and noun < 99:
		noun += 1
		nounF += 1
	elif data == "more" and noun == 99:
		noun = 0
		nounF = 0
		verb += 1
		verbF += 1
	elif type(data).__name__ == 'int' and data > 0:
		verb = data
		verbF = data
	elif type(data).__name__ == 'int' and data == 0:
		print("noun=" + str(noun))
		print("verb=" + str(verb))
		programArray = [int(a) for a in readInputFile()]
		programArray[1] = noun
		programArray[2] = verb
		pprint(intcode(programArray))
		break
	

	print("Done with one loop")
	#break

#pprint(intcode(programArray))