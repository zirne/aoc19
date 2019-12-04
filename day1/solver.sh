#!/bin/bash
#AOC day 1

output="output.txt"
input="input.txt"

echo -ne "" > $output
for i in $(cat input.txt | xargs); do

	echo $(echo "${i} / 3" | bc) -2 | bc >> $output

done
