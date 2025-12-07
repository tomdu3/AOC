"""
Day 7 Part 2: Quantum Tachyon Beam
This part uses the Many-Worlds Interpretation.
When a beam hits a splitter, it splits into two TIMELINES.
We need to count the total number of timelines (paths) the particle can take.
"""
from functools import cache

len_y = 0
len_x = 0
lines = []

def get_input():
    # Read grid from input.txt
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.read().splitlines()]
    return lines

def detect_first_split(lines):
    # Initializes globals and finds the first splitter encountered by the beam
    global len_y
    global len_x
    len_y = len(lines)
    len_x = len(lines[0])
    beams = set()
    
    # Locate start position 'S'
    for i in range(len_y):
        for j in range(len_x):
            if lines[i][j] == "S":
                beams.add((i, j))
                break
     
    # Trace the beam downwards until it hits a splitter '^'
    for i, j in beams:
        for y in range(i, len_y):
            if y+1 >= len_y:
                continue
            if lines[y+1][j] == "^":
                return (y+1, j)
    return None

@cache
def detect_split_paths(y, x):
    # Recursively counts timelines.
    # Returns the number of timelines generated from a split at (y, x).
    global len_y
    global len_x
    
    # Left Path: Go to (y, x-1) and keep going left until hitting something or edge
    left_y, left_x = y, x-1
    while left_y < len_y and lines[left_y][left_x] == ".":
        left_y += 1
    
    if left_y >= len_y:
        # Base case: Left path exits the manifold -> 1 timeline
        left_count = 1
    else:
        # Recursive case: Left path hits another splitter -> add its timelines
        left_count = detect_split_paths(left_y, left_x)

    # Right Path: Go to (y, x+1) and keep going right until hitting something or edge
    right_y, right_x = y, x+1
    while right_y < len_y and lines[right_y][right_x] == ".":
        right_y += 1
    
    if right_y >= len_y:
        # Base case: Right path exits the manifold -> 1 timeline
        right_count = 1
    else:
         # Recursive case: Right path hits another splitter -> add its timelines
        right_count = detect_split_paths(right_y, right_x)

    # Total timelines = timelines from left path + timelines from right path
    return left_count + right_count    

def main():
    global lines
    lines = get_input()
    # Find the coordinates where the first split happens
    first_split = detect_first_split(lines)
    
    if first_split:
        y, x = first_split
        # Calculate total number of timelines starting from the first split
        print(detect_split_paths(y, x))
    else:
        print("No split found")

if __name__ == "__main__":
    main()