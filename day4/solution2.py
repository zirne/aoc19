# Solution 2
def readInputFile(n):
	f = open(n, "r")
	d = f.read()
	f.close()
	return d.strip()

def checkNeverDecreaseRule(n):
	n = str(n)
	l = len(n)
	i = 0
	while i < l - 1:
		if int(n[i]) > int(n[i + 1]):
			return False
		i += 1
	return True

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

input = readInputFile("input.txt")

lowest = input.split("-")[0]
highest = input.split("-")[1]
current = int(input.split("-")[0])

resultArr = []

while current <= int(highest):
	if checkNeverDecreaseRule(current) and checkFinalRule(current):
		resultArr.append(current)
	current += 1

print(len(resultArr))