# useful Stuff
def readInputFile(n):
	f = open(n, "r")
	d = f.read()
	f.close()
	return d.strip()

def getInputData(n = None): # Format input data to the correct format for whatever we're doing
	if n == None:
		d = readInputFile("input.txt").split(",")
	else:
		d = readInputFile(n).split(",")
	return d

def inputAsStrings(n = None):
	return getInputData(n)

def inputAsInts(n = None):
	return [int(a) for a in getInputData(n)]