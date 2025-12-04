from pprint import pprint

def read_input(file_path):
    with open(file_path, "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] == '@':
                count += 1
    return count

def find_accessible_positions(grid):
    accessible_positions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                neighbors = count_neighbors(grid, x, y)
                if neighbors < 4:
                    accessible_positions.append((x, y))
    return accessible_positions

def main():
    grid = read_input("input.txt")
    total_removed = 0
    
    while True:
        accessible_positions = find_accessible_positions(grid)
        if not accessible_positions:
            break
        for x, y in accessible_positions:
            grid[y][x] = '.'
            total_removed += 1
    print(total_removed)

if __name__ == "__main__":
    main()