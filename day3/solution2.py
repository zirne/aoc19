from pprint import pprint
import numpy
#import sys

def getNewCoordinates(x,y,instruction):
    direction = instruction[:1]
    distance = int(instruction[1:])
    #print(direction)
    #print(distance)
    output = [] # array of coordinates
    i = 0
    while i < distance:
        if direction == "R" or direction == "U":
            if direction == "R":
                x += 1
            else:
                y += 1
        elif direction == "L" or direction == "D":
            if direction == "L":
                x -= 1
            else:
                y -= 1
        output.append(str(x)+","+str(y))
        i += 1
    return output


def readInputFile(filename):
	f = open(filename, "r")
	inputString = f.read()
	f.close()
	return inputString

inputData = readInputFile("test3.txt")

wirePaths = []
# Prepare Input Data
for a in inputData.split("\n"):
    if a != "":
        wirePaths.append(a)

pprint(wirePaths)

# Coordinate Magic, Create coordinates for everything
wirePathsPoints = []
for w in wirePaths:
    x=0 # R/L
    y=0 # U/D
    instructionSet = w.split(",")
    #coordinateSet = ["0,0"]
    coordinateSet = []
    for i in instructionSet:
        result = getNewCoordinates(x,y,i)
        for c in result:
            coordinateSet.append(c)
        cPos = result.pop()
        #print(cPos)
        x=int(cPos.split(",")[0])
        y=int(cPos.split(",")[1])
        #print(coordinateSet)
    wirePathsPoints.append(coordinateSet)
print(wirePathsPoints)




manhattanDistance = 9223372036854775807
manhattanDistanceList = []
intersectionCoordinates = []
for p1 in wirePathsPoints:
    for haystack in wirePathsPoints:
        #print(p1)
        #print(haystack)
        if p1 == haystack:
            #print("True")
            continue
        else:
            #print("Do stuff")
            print("Comparing lists...")
            counter = 0;
            for val in p1:
                if val in haystack:
                    mhdist = abs(int(val.split(",")[0])) + abs(int(val.split(",")[1]))
                    intersectionCoordinates.append(val)
                    manhattanDistanceList.append(str(mhdist) + "(" + val + ")")
                    if mhdist < manhattanDistance:
                        manhattanDistance = mhdist
                counter += 1
                if counter % 1000 == 0:
                    print("Processed " + str(counter) + "/" + str(len(p1)))


print()
print()
print()
print(manhattanDistanceList)
print("Lowest:")
print(manhattanDistance)

allIntersectionsDistance = []
allIntersectionsOrder = []

for w in wirePaths:
    x=0 # R/L
    y=0 # U/D
    dist=0
    instructionSet = w.split(",")
    #coordinateSet = ["0,0"]
    coordinateSet = []
    intersectionsDistance = []
    intersectionsOrder = []
    for i in instructionSet:

        result = getNewCoordinates(x,y,i)
        print(i)
        for c in result:
            dist += 1
            coordinateSet.append(c)
            #print("Checking if " + c + " exists in " + str(intersectionCoordinates) + "...")
            if c in intersectionCoordinates:
                print("Reached an intersection at " + c + " after travelling a distance of " + str(dist) +"!")
                intersectionsDistance.append(dist)
                intersectionsOrder.append(c)

                #break
        cPos = result.pop()

        #print(cPos)
        x=int(cPos.split(",")[0])
        y=int(cPos.split(",")[1])
        #print(coordinateSet)
    allIntersectionsDistance.append(intersectionsDistance)
    allIntersectionsOrder.append(intersectionsOrder)
    #wirePathsPoints.append(coordinateSet)
print()
print()
print(allIntersectionsDistance)
print(allIntersectionsOrder)

output = 9223372036854775807
for i in allIntersectionsDistance[0]:
#    print(i)
    indexForCoordinate = allIntersectionsDistance[0].index(i)
#    print(indexForCoordinate)
    # fetch which coordinates the distance is to
    coordinates = allIntersectionsOrder[0][indexForCoordinate]
#    print(coordinates)
    # fetch other index
    otherIndex = allIntersectionsOrder[1].index(coordinates)
#    print(otherIndex)
    otherValue = allIntersectionsDistance[0][otherIndex]
#    print(otherValue)
    if int(i) + int(otherValue) < output:
        output = int(i) + int(otherValue)



print(output)
exit()
#    for p2 in wirePathsPoints[ciA]:
#        if ciA == ciB:
#            print("skipping comparing to itself")
#            ciB += 1
#            continue
#        else:
#            print("comparing "++" to other")
#        if p1[ciA] in p2[ciB]:
#            print(p1[ciA])
#        ciB += 1
#    ciA += 1
#    ciB = 0
    #exit()
