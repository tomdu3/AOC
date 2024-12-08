# Input parsing
in_put = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# read input from the file
with open('input08.txt') as f:
    in_put = f.read()
in_put = [line for line in in_put.split('\n') if line]
rows = len(in_put)
cols = len(in_put[0])
antennae = {}

# Collect positions of antennas by frequency
for y, row in enumerate(in_put):
    for x, ch in enumerate(row):
        if ch != ".":
            if ch not in antennae:
                antennae[ch] = []
            antennae[ch].append((y, x))

antinodes = set()

# Helper function to check if a position is within bounds
def is_within_bounds(y, x, rows, cols):
    return 0 <= y < rows and 0 <= x < cols

# Process each frequency's antennas
for same_antennae in antennae.values():
    for i in range(len(same_antennae)):
        for j in range(i + 1, len(same_antennae)):
            y1, x1 = same_antennae[i]
            y2, x2 = same_antennae[j]

            # Calculate potential antinodes
            antinode_y1, antinode_x1 = 2 * y1 - y2, 2 * x1 - x2
            antinode_y2, antinode_x2 = 2 * y2 - y1, 2 * x2 - x1

            # Add valid antinodes within bounds
            if is_within_bounds(antinode_y1, antinode_x1, rows, cols):
                antinodes.add((antinode_y1, antinode_x1))
            if is_within_bounds(antinode_y2, antinode_x2, rows, cols):
                antinodes.add((antinode_y2, antinode_x2))

# Output the count of unique antinodes
print(len(antinodes))

