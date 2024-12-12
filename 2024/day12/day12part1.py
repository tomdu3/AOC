from pprint import pprint

def make_grid(in_put):
    grid = []
    for line in in_put.strip().split("\n"):
        grid.append(list(line))
    return grid

def flood_fill(grid, visited, y, x):
    rows, cols = len(grid), len(grid[0])
    symbol = grid[y][x]
    stack = [(y, x)]
    region = []
    perimeter = 0

    while stack:
        cy, cx = stack.pop()
        if visited[cy][cx]:
            continue

        visited[cy][cx] = True
        region.append((cy, cx))

        # Check all 4 neighbors
        for ny, nx in [(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)]:
            if 0 <= ny < rows and 0 <= nx < cols:
                if grid[ny][nx] == symbol and not visited[ny][nx]:
                    stack.append((ny, nx))
                elif grid[ny][nx] != symbol:
                    perimeter += 1
            else:
                perimeter += 1

    return region, perimeter

def calculate_fencing_cost(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_cost = 0

    for y in range(rows):
        for x in range(cols):
            if not visited[y][x]:
                region, perimeter = flood_fill(grid, visited, y, x)
                area = len(region)
                cost = area * perimeter
                total_cost += cost

    return total_cost

# Input data
in_put = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# take input from file
with open("input12.txt") as f:
    in_put = f.read().strip()

# Prepare the grid
grid = make_grid(in_put)

# Calculate the total fencing cost
total_cost = calculate_fencing_cost(grid)
print(f"Total cost of fencing: {total_cost}")
