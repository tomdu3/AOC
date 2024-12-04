def count_xmas_occurrences(grid):
    word = "XMAS"
    len_word = len(word)
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def check_direction(r, c, dr, dc):
        # Check the word in a specific direction
        for i in range(len_word):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
                return False
            r += dr
            c += dc
        return True

    # Directions to check: right, left, down, up, and 4 diagonals
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-Right
        (1, -1), # Down-Left
        (-1, 1), # Up-Right
        (-1, -1) # Up-Left
    ]
    
    # Loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check all directions from each cell
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

# Example usage:
word_search = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

with open("input04.txt") as f:
    word_search = [line.strip() for line in f]

print(count_xmas_occurrences(word_search))