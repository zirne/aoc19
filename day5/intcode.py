# Intcode computer
import pprint
import warnings
import useful_functions as useful

class intcodeData:
	raw = None
	position = None
	program = None
	opcode = None
	abcde = []
	originalProgram = None
	nextPosition = None
	stepCounter = 0
	modeFlags = []
	paramvalsForOpcodes = []
	paramCount = [0,4,4,1,1]
	stack = []
	prgStack = []
	lastInstruction = ""

	def printDebugInfo(self):
		print("Raw:" + str(self.raw))
		print("Position:" + str(self.position))
		print("Opcode:" + str(self.opcode))
		print("nextPosition:" + str(self.nextPosition))
		print("stepCounter:" + str(self.stepCounter))
		print("modeFlags:" + str(self.modeFlags))
		print("paramvalsForOpcodes:" + str(self.paramvalsForOpcodes))
		#print("program:" + str(self.program))

		print("Program Status:")
		self.printReadableProgram()


		self.printLastNstack(10)


		exit()

	def printLastNstack(self, n):
		s = list(reversed(self.stack))
		c = 1
		for d in s:
			if c <= n:
				print(d)
			else:
				break



	def printReadableProgram(self):
		a = []
		i = 0
		while i < len(self.program):
			c = i+1
			if i == self.position:
					a.append(">>>" + str(self.program[i]) + "<<<")
			else:
				a.append(self.program[i])
			if c % 10 == 0:
				
				print(str(a))
				a = []
			i += 1

	def fill_paramCount(self):
		while len(self.paramCount) < 100:
			self.paramCount.append(0)

	def setABCDE(self, i = None):
		if i == None:
			i = self.raw
		s = str(i)
		while len(s) < 5:
			s = "0" + s
		a = list(s)
		self.abcde = [int(c) for c in a]

	def setOpcodeFromInt(self, i = None):
		if i == None:
			i = self.raw
		s = str(i)
		while len(s) < 2:
			s = "0" + s
		s = s[-2:]
		try:
			self.opcode = int(s.lstrip("0"))
		except:
			print("Could not fetch opcode from value: " + str(self.raw) + " found at address " + str(self.position) + "!")
			#print(str(i))
			#print(s)
			#print(self.position)
			#print(self.program)
			exit()

	def opDebugP(self, op, data, prd, wp, org):
		o = ""
		if op == 1:
			o = "+"
		if op == 2:
			o = "*"
		data = [str(a) for a in data]
		if len(data)>1:
			d = o.join([data[0],data[1]])
		else:
			d = str(data[0])
		#print(data)
		return "OP" + str(op) + " @ pos:" + str(self.position) + " - Writing " + str(prd) + " (" + d + ")" + " to address " + str(wp) + " (Original data:" + str(org) + ")"

	def op1(self): # value1, value2, address to write to
		d = self.paramvalsForOpcodes
		wp = self.program[self.position+3]

		prd = d[0] + d[1]
		#self.lastInstruction = "OP1@" +str(self.position) + " - Writing " + str(d[0] + d[1]) + "(" + str(d[0]) + "+" + str(d[1]) + ")" + " to address " + str(wp)
		#self.lastInstruction = self.opDebugP(1,d,prd,wp,self.program[wp])
		#print("OP1@" +str(self.position) + " - Writing " + str(d[0] + d[1]) + "(" + str(d[0]) + "+" + str(d[1]) + ")" + " to address " + str(wp))



		print(self.opDebugP(1,d,prd,wp,self.program[wp]))



		self.program[wp] = prd
		self.position += 4
	def op2(self): # value1, value2, address to write to
		d = self.paramvalsForOpcodes
		wp = self.program[self.position+3]
		prd = d[0] * d[1]
		#self.lastInstruction = "OP2@" +str(self.position) + " - Writing " + str(d[0] * d[1]) + "(" + str(d[0]) + "*" + str(d[1]) + ")" + " to address " + str(wp)
		#print("OP2@" +str(self.position) + " - Writing " + str(d[0] * d[1]) + "(" + str(d[0]) + "*" + str(d[1]) + ")" + " to address " + str(wp))
		#self.lastInstruction = self.opDebugP(2,d,prd,wp,self.program[wp])
		print(self.opDebugP(2,d,prd,wp,self.program[wp]))
		self.program[wp] = prd
		self.position += 4
		#print()
	def op3(self):
		#data = input("Enter input:")
		data = "1"
		wp = self.program[self.position+1]
		print(self.opDebugP(3,data,data,wp,self.program[wp]))
		#self.lastInstruction = self.opDebugP(3,data,data,wp,self.program[wp])
		#self.lastInstruction = "OP3@" +str(self.position) + " - Writing " + data + " to address " + str(wp)
		#print("OP3@" +str(self.position) + " - Writing " + data + " to address " + str(wp))
		self.program[wp] = int(data)
		self.position += 2
		#print()
	def op4(self):
		d = self.paramvalsForOpcodes
		#print(self.program[self.position + 1])
		if (d[0]) != 0:
			print("Error occured!")
			print("Error code: " + str(d[0]))
			self.printDebugInfo()
		self.position += 2
	def op99(self):
		print()
		print()
		print()
		print("Result of the Program:")
		print(self.program)
		exit()

	def fixModeFlags(self):
		s = str(self.raw)
		while len(s) < 5:
			s = "0" + s
		a = list(s)
		self.modeFlags = [int(c) for c in a]
		self.modeFlags.pop()
		self.modeFlags.pop()
		self.modeFlags = list(reversed(self.modeFlags))
		# remove unused params if there are any
		while len(self.modeFlags) > self.paramCount[self.opcode]:
			self.modeFlags.pop()
		#	print()



	def fixParams(self):
		try:
			i = 0
			out = []
			while i < len(self.modeFlags):
				paramPointer = i + 1
				debugVar = self.position + paramPointer
				data = self.program[self.position + paramPointer]
				if self.modeFlags[i] == 1:
					out.append(data)
				else:
					out.append(self.program[data]) 
				i += 1
			self.paramvalsForOpcodes = out
		except Exception as e:
			print("Could Not fix parameters!")
			print(e)
			print("i=" + str(i))
			print("debugVar=" + str(debugVar))
			print(data)
			self.printDebugInfo()


	def processStep(self):
		# Initial stuff, set current opcode and flags
		self.raw = self.program[self.position]
		self.setABCDE(self.raw)
		self.setOpcodeFromInt(self.raw)
		self.fixModeFlags()
		self.setOpcodeFromInt(self.raw)
		self.fixParams()






		#print(self)
		#print(self.opcode)








		if(self.opcode == 1):
			self.op1()
		if(self.opcode == 2):
			self.op2()
		if(self.opcode == 3):
			p1 = self.program[self.position+1]
			self.op3()
		if(self.opcode == 4):
			#p1 = self.program[self.position+1]
			self.op4()
		if(self.opcode == 99):
			self.op99()
		#exit()

		# Update current opcode stuff
		#self.raw = self.program[self.position]
		#self.setABCDE(self.raw)
		#self.setOpcodeFromInt(self.raw)
		self.stack.append(self.lastInstruction)
		self.prgStack.append(self.program)



	def runMe(self):
		print("Starting to process all steps...")
		print("Program is " + str(len(self.program)) + " datapoints long")
		while True:
			self.processStep()

	def getValueFromPosition(self,i):
		try:
			return self.program[self.program[i]]
		except:
			print("Could not complete getValueFromPosition!")
			print(i)
			print(self.program[i])
			exit()

	# Cool code that print itself nicely
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def __init__(self, position, program):
		self.position = position
		self.originalProgram = program # A copy of the original for debugging
		self.program = program

		self.fill_paramCount()
		#print("Instance started")
		#print(self.raw)








def run(code): # Takes the program as an array of ints
	warnings.filterwarnings("error")
	#try:
	if isinstance(code[0], int) == False:
		#print("Got Strings")
		code = [int(a) for a in code]
	#print(code)
	intcode = code
	running = True
	pos = 0
	while running:
		#pprint("parsing position " + str(pos))
		op = intcode[pos]
		#print("OP="+str(op))
		#print("POS="+str(pos))
		ni = 0 # default value to add to pointer jump (Yes, this can create an infinite loop)


		data = intcodeData(pos, intcode)
		data.runMe()
		#print(data)
		exit()


		if(op == 1):
			src1 = intcode[pos+1]
			src2 = intcode[pos+2]
			dst = intcode[pos+3]
			intcode[dst] = intcode[src1] + intcode[src2]
			ni = 4
		elif(op == 2):
			src1 = intcode[pos+1]
			src2 = intcode[pos+2]
			dst = intcode[pos+3]
			intcode[dst] = intcode[src1] * intcode[src2]
			ni = 4
		elif(op == 3):
			src1 = intcode[pos+1]
			ni = 2
		elif(op == 4):
			src1 = intcode[pos+1]
			ni = 2
		elif(op == 99):
			running = False
			break
		else:









			print()
			#print(op)
			#print(pos)
			#raise UserWarning("Invalid OPCODE: " + str(op) + " found at position: " + str(pos) + "!")
			#raise UserWarning(op, pos)

		# Move pointer to next instruction (ni)
		pos += ni
		#exit()
	return intcode
	#except:

		#print("Invalid OPCODE: " + str(op) + " found at position: " + str(pos) + "!")
		#exit()
	#return ",".join([str(a) for a in intcode])



# Run program here

#pprint(intcode(a))