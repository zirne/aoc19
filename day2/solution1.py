f = open("fixedInput.txt", "r")
prg = f.read()
prg = prg.replace("\n","")
prg = prg.strip()
prgArray = prg.split(",")
f.close()
#print(prgArray[2])


def parseInstruction(i, position):
	#print("Parsing instruction " + str(i) + " at position " + str(position))
	if i == "1":
		#print("Addition instruction")
		nPos1=int(prgArray[position + 1]) # noun
		nPos2=int(prgArray[position + 2]) # verb
		nPos3=int(prgArray[position + 3])
		print("Adding " + prgArray[nPos1] + " found at position " + str(nPos1) + " read from " + str(position + 1))
		print("Adding " + prgArray[nPos2] + " found at position " + str(nPos2) + " read from " + str(position + 2))
		print("Result: " + str(int(prgArray[nPos1]) + int(prgArray[nPos2])) + ", Placing at position " + str(nPos3) + " read from " + str(position + 3))
		prgArray[nPos3] = str(int(prgArray[nPos1]) + int(prgArray[nPos2]))
		return 1
	if i == "2":
		#print("Multiplication instruction")
		nPos1=int(prgArray[position + 1]) # noun
		nPos2=int(prgArray[position + 2]) # verb
		nPos3=int(prgArray[position + 3])
		print("Multiplying " + prgArray[nPos1] + " found at position " + str(nPos1) + " read from " + str(position + 1))
		print("Multiplying " + prgArray[nPos2] + " found at position " + str(nPos2) + " read from " + str(position + 2))
		print("Result: " + str(int(prgArray[nPos1]) * int(prgArray[nPos2])) + ", Placing at position " + str(nPos3) + " read from " + str(position + 3))
		prgArray[nPos3] = str(int(prgArray[nPos1]) * int(prgArray[nPos2]))
		return 2
	if i == "99":
		return 99

instruction=0
position=0
while 1 == 1:
	instruction = prgArray[position]
	print("Parsing instruction " + str(instruction) + " at position " + str(position))
	if int(instruction) == 99:
		#print("brejka?")
		break
	else:
		parseInstruction(prgArray[position], position)
		position = position + 4
		data = ','.join(prgArray)
		print(data)
	#break
print("")
print("")
print("")
print("Before:")
print(prg)
result = ','.join(prgArray)
#result = prgArray.join(",")
print("After")
print(result)


#for x in f:
#	result = calc_fuel(x)
#	if result is not None and result > 0:
#		print(result)
#		outputArr.append(result)


