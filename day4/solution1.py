# Solution 1
def readInputFile(filename):
	f = open(filename, "r")
	inputString = f.read()
	f.close()
	return inputString

input = readInputFile("input.txt").strip()

print(input)

lowest = input.split("-")[0]
highest = input.split("-")[1]
current = int(input.split("-")[0])

print(lowest)
print(highest)

def checkNeverDecreaseRule(n):
	n = str(n)
	l = len(n)
	i = 0
	while i < l - 1:
	#	print("comparing " + n[i] + " with " + n[i + 1] + "...")
		if int(n[i]) > int(n[i + 1]):
			return False
		i += 1
	return True

def checkHasAdjacentSame(n):
	n = str(n)
	l = len(n)
	i = 0
	adjCount = 0
	while i < l - 1:
	#	print("comparing " + n[i] + " with " + n[i + 1] + "...")
		if n[i] == n[i + 1]:
			adjCount += 1
		i += 1
	if adjCount >= 1:
		return True
	else:
		return False

resultArr = []

while current <= int(highest):
	if checkNeverDecreaseRule(current) and checkHasAdjacentSame(current):
		resultArr.append(current)
	#print(checkNeverDecreaseRule(lowest))
	#print(checkHasAdjacentSame(lowest))
	
	current += 1

print(len(resultArr))