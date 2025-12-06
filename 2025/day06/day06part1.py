import math

def load_input():
    """
    Reads 'input.txt' and processes lines.
    Lines are converted to a list of integers (for numbers) and strings (for operators or placeholders).
    """
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines):
        # Parse each line: keep integers as ints, everything else (like operatos) as strings
        values = [int(value) if value.isnumeric() else value for value in line.strip().split()]
        lines[idx] = values

    return lines


def calculate(*args, operator):
    """
    Performs the specified arithmetic operation on the provided arguments.
    Supported operators: '+' (sum) and '*' (product).
    """
    match operator:
        case "+":
            return sum(args)
        case "*":
            return math.prod(args)


def main():
    total = 0
    lines = load_input()
    # The problem asks to process columns. 
    # 'lines' is a list of rows, so we iterate through the index of the first row (assuming all rows are equal length)
    # to access the column index 'idx'.
    for idx in range(len(lines[0])):
        # Extract the column values: 
        #   lines[:-1] are the number rows.
        #   lines[-1] is the operator row.
        # We collect numbers from the current column 'idx' across all number rows.
        # Then we call calculate with these numbers and the operator at the bottom of the column.
        temp = calculate(*[lines[i][idx] for i in range(len(lines[:-1]))], operator=lines[-1][idx])
        total += temp
    print(total)

main()