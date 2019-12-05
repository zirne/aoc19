from pprint import pprint

# Solution 2
def readInputFile(n):
	f = open(n, "r")
	d = f.read()
	f.close()
	return d.strip()

def getInputData(): # Format input data to the correct format for whatever we're doing
	d = readInputFile("input.txt").split(",")
	return d

def inputAsStrings():
	return getInputData()

def inputAsInts():
	return [int(a) for a in getInputData()]




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



# Run program here
a = inputAsInts();
a[1] = 12
a[2] = 2

pprint(intcode(a))