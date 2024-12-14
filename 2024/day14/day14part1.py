from pprint import pprint

in_put = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# test data 
# WIDTH = 11
# HEIGHT = 7

in_put = open("input14.txt").read().strip()

WIDTH = 101
HEIGHT = 103

def clean_input(in_put):
    data = []
    for line in in_put.split("\n"):
        p, v = line.split()
        pos = tuple(map(int, p[2:].split(',')))
        vel = tuple(map(int, v[2:].split(',')))
        data.append(pos + vel)
    return data

data = clean_input(in_put)

def move(data, seconds):
    final_move_grid = []
    for px, py, vx, vy in data:
        final_move_grid.append(((px + vx * seconds) % WIDTH, (py + vy * seconds) % HEIGHT))
    return final_move_grid

def display_grid(data):
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for x,y in data:
        grid[y][x] +=1
    for line in [[ '.' if ch == 0 else ch for ch in grid_line] for grid_line in grid]:
        print(''.join([f"{el}" for el in line]))
    return grid

def calc_robots_quadrants(data):
    x_half = WIDTH // 2
    y_half = HEIGHT // 2
    quadrants = {}
    for x,y in data:
        if x < x_half and y < y_half:
            quadrants[0] = quadrants.get(0, 0) + 1
        if x < x_half and y > y_half:
            quadrants[1] = quadrants.get(1, 0) + 1
        if x > x_half and y > y_half:
            quadrants[2] = quadrants.get(2, 0) + 1
        if x > x_half and y < y_half:
            quadrants[3] = quadrants.get(3, 0) + 1
    result = 1
    for val in quadrants.values():
        result *= val
    return result

move_data = move(data, 100)
grid = display_grid(move_data)
    
print(calc_robots_quadrants(move_data))
