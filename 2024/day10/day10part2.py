from pprint import pprint
from collections import deque

in_put = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

with open("input10.txt") as f:
    in_put = f.read()

def make_grid(in_put):
    grid = []
    for line in in_put.strip().split("\n"):
        grid.append([int(x) for x in line])
    return grid

grid = make_grid(in_put)
pprint(grid)

def find_starting_nodes(grid):
    starting_nodes = []
    y_axis = len(grid)
    x_axis = len(grid[0])
    for y in range(y_axis):
        for x in range(x_axis):
            if grid[y][x] == 0:
                starting_nodes.append((y, x))
    return starting_nodes

starting_nodes = find_starting_nodes(grid)
pprint(starting_nodes)

def find_paths(grid, y, x):
    rows, cols = len(grid), len(grid[0])
    q = deque([(y, x)])
    visited = {(y, x): 1}  # Initialize a dictionary with 1 value for the visited node
    summits = 0

    while q:
        current_y, current_x = q.popleft()
        if grid[current_y][current_x] == 9:
            summits += visited[(current_y, current_x)]
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_y, new_x = current_y + dy, current_x + dx
            # Check bounds
            if new_y < 0 or new_y >= rows or new_x < 0 or new_x >= cols:
                continue
            # Check height difference
            if grid[new_y][new_x] != grid[current_y][current_x] + 1:
                continue
            # Check if already visited
            if (new_y, new_x) in visited:
                visited[(new_y, new_x)] += visited[(current_y, current_x)]
                continue
            visited[(new_y, new_x)] = visited[(current_y, current_x)]
            q.append((new_y, new_x))  # Continue the path
    return summits

def calculate_score(grid, starting_nodes):
    sum_of_summits = 0
    for y, x in starting_nodes:
        summits = find_paths(grid, y, x)
        sum_of_summits += summits
    return sum_of_summits

score = calculate_score(grid, starting_nodes)
print(f"Sum of all trailhead scores: {score}")


