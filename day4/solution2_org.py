# Solution 2
def readInputFile(filename):
	f = open(filename, "r")
	inputString = f.read()
	f.close()
	return inputString

input = readInputFile("input.txt").strip()

lowest = input.split("-")[0]
highest = input.split("-")[1]
current = int(input.split("-")[0])

def checkNeverDecreaseRule(n):
	n = str(n)
	l = len(n)
	i = 0
	while i < l - 1:
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
		if n[i] == n[i + 1]:
			adjCount += 1
		i += 1
	if adjCount >= 1:
		return True
	else:
		return False

def checkFinalRule(n):
	n = str(n)
	for i in n:
		counter = 0
		for ir in n:
			if i == ir:
				counter += 1
		if counter == 2:
			return True
	return False	

resultArr = []

while current <= int(highest):
	if checkNeverDecreaseRule(current) and checkHasAdjacentSame(current) and checkFinalRule(current):
		resultArr.append(current)
	current += 1

print(len(resultArr))