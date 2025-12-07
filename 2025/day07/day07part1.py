"""
Day 7 Part 1: Classical Tachyon Beam
The beam splits at '^' into left and right paths.
We track beams row by row.
"""

def get_input():
    # Read the grid from input.txt
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.read().splitlines()]
    return lines

def detect_split(lines):
    beams = set()
    len_y = len(lines)
    len_x = len(lines[0])
    split_count = 0
    
    # Locate the starting point 'S'
    for i in range(len_y):
        for j in range(len_x):
            if lines[i][j] == "S":
                beams.add((i, j))
                break
     
    # Iterate through each row to simulate beam propagation
    for y in range(1, len_y):
       new_beams = set()
       for i, j in beams:
          if y+1 >= len_y:
            continue
          # Beams move downwards. Check the cell directly below.
          if lines[y+1][j] == "^":
            # If it's a splitter, the beam splits left and right (j-1, j+1)
            new_beams.add((y+1, j-1))
            new_beams.add((y+1, j+1))
            split_count += 1
          else:
            # Otherwise, the beam continues straight down
            new_beams.add((y+1, j))
       beams = new_beams

    return split_count

def main():
    lines = get_input()
    print(detect_split(lines))

if __name__ == "__main__":
    main()