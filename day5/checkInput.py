# get opcodes in input
import useful_functions as useful
import pprint

input = useful.getInputData("input.txt")

i=0
while i < len(input):
	if i % 4 == 0:
		print(input[i])
	i += 1