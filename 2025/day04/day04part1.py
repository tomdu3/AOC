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

def main():
    grid = read_input("input.txt")
    accessible_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                neighbors = count_neighbors(grid, x, y)
                if neighbors < 4:
                    accessible_count += 1
    print(accessible_count)

if __name__ == "__main__":
    main()