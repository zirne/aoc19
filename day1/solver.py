import math
outputArr = []

def calc_fuel(inputStr):
	#print(inputStr)
	inputStr = str(inputStr)
	inputStr = inputStr.replace("\n","")
	inputStr = inputStr.strip()
	if inputStr != "":
		inputVal = int(inputStr)
	#	print(inputVal)
		finalVal = math.floor(inputVal / 3) - 2
	#	print(str(inputVal) + " requires " + str(finalVal) + " fuel.")
		if finalVal > 0:
			returnVal = finalVal + calc_fuel(finalVal)
		else:
			returnVal = 0
		return returnVal
		
f = open("input.txt", "r")
for x in f:
	result = calc_fuel(x)
	if result is not None and result > 0:
		print(result)
		outputArr.append(result)
f.close()

print(math.fsum(outputArr))
