def count_xmas_pattern(grid):
    count = 0

    # Define the valid diagonal patterns
    search_combinations = ["MMSS", "SSMM", "MSSM", "SMMS"]
    
    # Loop through each cell, skipping the borders
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] == "A":
                # Extract diagonal ends
                diagonal_ends = "".join([grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c -1]])

                # Check if the diagonal ends match any of the valid patterns
                if diagonal_ends in search_combinations:
                    count += 1

    
    return count

# Sample word search
word_search = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "..........",
]


# with open("input04.txt") as f:
#     word_search = [line.strip() for line in f]

print(count_xmas_pattern(word_search))
