import sys
import re

with open("input.txt") as f:
    ranges = [(int(start), int(end)) for range in f.read().strip().split(',') for start, end in [range.split('-')]]
result = 0
for start, end in ranges:
    is_invalid = False
    for i in range(start, end+1):
        id = str(i)
        len_id = len(id)
        for size in range(1, len_id//2+1):
            if len_id % size == 0:
                repeat_part = id[:size]
                if repeat_part * (len_id // size) == id:
                    is_invalid = True
                    break
        if is_invalid:
            result += i
            is_invalid = False
print(result)

