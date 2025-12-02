import sys
import re

with open("input.txt") as f:
    ranges = [(int(start), int(end)) for range in f.read().strip().split(',') for start, end in [range.split('-')]]
result = 0
for start, end in ranges:
     for i in range(start, end+1):
         id = str(i)
         if (length:=len(id)) % 2 == 0 and id[:length//2] == id[length//2:]:
            result += i
print(result)
