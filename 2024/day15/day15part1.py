def parse_input(in_put):
    grid_str, moves = in_put.strip().split('\n\n')
    # Split map into rows
    grid = grid_str.strip().split('\n')
    grid = [[symbol for symbol in line] for line in grid]
    moves = moves.replace("\n", "")  # Remove newlines from move sequence
    return grid, moves

# Example input
in_put = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

in_put = open("input15.txt", "r").read()
grid, moves = parse_input(in_put)

def get_coordinates(grid, moves):
    rows = len(grid)
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "@":
                break
        else:
            continue
        break

    for move in moves:
        direction_x = {"^": -1, "v": 1}.get(move, 0)
        direction_y = {"<": -1, ">": 1}.get(move, 0)
        targets = [(x, y)]
        current_x = x
        current_y = y
        go = True
        while True:
            current_x += direction_x 
            current_y += direction_y
            symbol = grid[current_x][current_y]
            if symbol == "#":
                go = False
                break
            if symbol == "O":
                targets.append((current_x, current_y))
            if symbol == ".":
                break
        if not go: continue
        grid[x][y] = "."
        grid[x + direction_x ][y + direction_y] = "@"
        for box_x, box_y in targets[1:]:
            grid[box_x + direction_x][box_y + direction_y] = "O"
        x += direction_x 
        y += direction_y

    coordinates = []
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "O":
                coordinates.append((x, y))

    return coordinates

def calculate_coordinates(coordinates):
    sum_of_coordinates = 0
    for x,y in coordinates:
        sum_of_coordinates += 100 * x + y

    return sum_of_coordinates

        
print(get_coordinates(grid, moves))
coordinates = get_coordinates(grid, moves)

print(calculate_coordinates(coordinates))


