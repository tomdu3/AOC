from pprint import pprint


def make_grid(input_text):
    # Converts the input text into a grid of characters
    return [list(line) for line in input_text.strip().split("\n")]


def find_symbol_region(symbol, grid):
    # Finds all the positions of a given symbol in the grid
    rows = len(grid)
    cols = len(grid[0])
    positions = [(y, x) for y in range(rows) for x in range(cols) if grid[y][x] == symbol]
    return positions


def get_regions(symbols, grid):
    # Finds regions for each symbol and returns their coordinates
    region_dict = {}
    for symbol in symbols:
        region_dict[symbol] = find_symbol_region(symbol, grid)
    return region_dict


def count_sides(region):
    # Counts the sides based on the corner configurations
    corner_candidates = set()
    
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    
    corners = 0
    for cr, cc in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]]
        number = sum(config)
        
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    
    return corners

def calculate(grid, symbols):
    # Calculates the total price by summing the size of each region multiplied by its side count
    regions = get_regions(symbols, grid)
    total_price = 0
    for symbol, region in regions.items():
        number_of_sides = count_sides(region)
        total_price += number_of_sides * len(region)
        print(symbol, number_of_sides)  # For debugging, you can remove this later
    return total_price

# Input data
input_text = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# Prepare the grid
grid = make_grid(input_text)
symbols = set(symbol for row in grid for symbol in set(row))  # Set of unique symbols

# Calculate the result
result = calculate(grid, symbols)
print(result)
