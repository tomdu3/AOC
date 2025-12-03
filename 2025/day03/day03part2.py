import sys
import re

# read input
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    

def max_joltage(line):
    nums = list(line)
    max_len = 12
    n = len(nums)
    to_remove = n - max_len
    stack = []
    
    for i, num in enumerate(nums):
        while to_remove > 0 and stack and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)
    
    while len(stack) > max_len:
        stack.pop()
    return int(''.join(stack))

def calculate_joltage(lines):
    result = 0
    for line in lines:
        result += max_joltage(line)
    return result
    
print(calculate_joltage(lines))

