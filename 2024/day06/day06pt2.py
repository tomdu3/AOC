import numpy as np

# in_put = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

with open('input06.txt') as f:
    in_put = f.read()

def print_grid(grid):
    for line in grid:
        print(line)
    print()

direction_change = [(-1,0), (0, 1), (1, 0), (0, -1)]

def convert_to_grid(input):
    grid = []
    line_number = 0
    starting_position = (0,0)
    for line in in_put.split('\n'):
        if not line:
            continue
        grid.append([])
        ch_number = 0
        for ch in line:
            match ch:
                case '.':
                    grid[line_number].append(0)
                case '#':
                    grid[line_number].append(1)
                case _:
                    grid[line_number].append(0)
                    starting_position = (line_number, ch_number)
            ch_number +=1
        line_number +=1

    grid_np = np.array(grid)
    y, x = starting_position[0], starting_position[1]

    return(grid_np, y, x)

def loop_locked(grid, y, x):
    change_direction = 0
    seen = set()
    while True:
        if y == len(grid) - 1 or x == len(grid[0]) - 1 or y == 0 or x == 0:
            break
        move_y, move_x = direction_change[change_direction % 4]
        move = y + move_y, x + move_x
        if grid[move] == 1:
            if (move, change_direction % 4) in seen:
                return True
            seen.add((move, change_direction % 4))
            change_direction += 1
            continue

        y, x = move

    return False

def find_loop_locks(grid_input, y, x):
    count = 0
    grid = grid_input.copy()
    len_y, len_x = grid.shape
    count_loop_locks = 0

    for j in range(len_y):
        for i in range(len_x):
            # Only test empty cells and avoid starting position
            if grid[j, i] == 0 and not (j,i) == (y,x):
                # Temporarily place an obstacle
                grid[j, i] = 1
                if loop_locked(grid, y, x):
                    count_loop_locks += 1
                # Restore the grid
                grid[j, i] = 0

    return count_loop_locks

# Convert input to grid and find the solution
grid, y, x = convert_to_grid(in_put)
print(loop_locked(grid, y, x))
count_loop_locks = find_loop_locks(grid, y, x)
print(count_loop_locks)
