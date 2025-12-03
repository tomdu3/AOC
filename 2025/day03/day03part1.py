import sys
import re

# read input
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]



def max_joltage(line):
    highest = 0
    for i, num in enumerate(line):
        for j, num2 in enumerate(line[i+1:]):
            if int(num+num2) > highest:
                highest = int(num+num2)
    return highest

def calculate_joltage(lines):
    result = 0
    for line in lines:
        result += max_joltage(line)
    return result
    
print(calculate_joltage(lines))
