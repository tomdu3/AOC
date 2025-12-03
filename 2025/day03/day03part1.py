import sys
import re

# read input
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split()


def max_joltage(line):
    highest = 0
    for i, num in enumerate(line[:-1]):
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
