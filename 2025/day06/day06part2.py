import math

def load_input():
    """
    Reads 'input.txt' and reconstructs the numbers which are written vertically.
    
    The input format is tricky: numbers are written vertically in columns.
    However, multiple 'problems' are on the same lines, separated by spaces.
    This function parses the input to group these vertical numbers correctly.
    """
    with open("input.txt", "r") as f:
        lines = f.readlines()
    verify_lines = lines.copy()
    len_values = []
    # The last line contains the operators (+, *) for each problem column
    operators = lines[-1].strip().split()
    
    # First pass: determine the width (number of columns) of each number block
    for idx, line in enumerate(lines[:-1]):
        # Get values and their string lengths from each line
        values = [(int(value), len(value)) for value in line.strip().split()]
        lines[idx] = [value[0] for value in values]
        if idx < len(lines) - 1:
            if not len_values:
                len_values = [value[1] for value in values]
            else:
                # Keep track of the maximum width found for each column block so far
                len_values = [max(len_values[id], value[1]) for id, value in enumerate(values)]
    
    idx = 0
    # Prepared list to hold the reconstructed vertical strings for each row
    lines = [[] for _ in range(len(lines[:-1]))]
    
    # Second pass: Extract the vertical slices based on the widths calculated above
    for i, lenght in enumerate(len_values):
        for j, line in enumerate(verify_lines[:-1]):
            # Slice the line to get the chunk for the current number column
            num_str = line[idx:idx+lenght]
            new_num_str = ""
            # Replace spaces within the number block with '0' to handle alignment.
            # Note: The logic 'else: new_num_str += "0"' for spaces suggests treating spaces as 0s.
            for ch in num_str:
                if ch != " ":
                    new_num_str += ch
                else:
                    new_num_str += "0"
            lines[j].append(new_num_str)

        # Move index to the next block (length + 1 for space separator)
        idx += lenght + 1
    
    lines.append(operators)
    return lines


def calculate(*args, operator):
    """
    Standard arithmetic operation handler.
    """
    match operator:
        case "+":
            return sum(args)
        case "*":
            return math.prod(args)

def calculate_line(*column, operator):
    """
    Calculates the result for a single vertical problem column.
    
    The input 'column' contains strings of digits that form numbers when read top-to-bottom.
    But the problem statement in Part 2 says "Cephalopod math is written right-to-left in columns",
    so we reconstruct numbers from these vertical slices.
    
    The logic seems to be:
    1. 'column' has the vertical slices for the operands.
    2. We reconstructed them somewhat in load_input, but here we finalize the number construction.
    3. The loop logic `for j in range(len(new_column)): num += new_column[j][-i-1]` 
       suggests we are reading digits from right-to-left to form the actual integer values.
    """
    column_nums = []
    new_column = []
    
    # Clean up the column data: restore spaces where we might have put 0s if they were padding, 
    # to handle the vertical alignment correctly.
    for num in column:
        new_num = ""
        for i in range(len(num)):
            if num[i] == "0":
                new_num += " "
            else:
                new_num += num[i]
        new_column.append(new_num)
    
    # Reconstruct the integers.
    # It loops through the character positions (width of the column block).
    for i in range(len(new_column[0])):
        num = ""
        # It concatenates the character at index -i-1 (right-to-left) from each row 'j'.
        # This implies that we are reading columns of the text block as numbers.
        for j in range(len(new_column)):
            num += new_column[j][-i-1]
        column_nums.append(int(num))
        
    return calculate(*column_nums, operator=operator)


def main():
    total = 0
    lines = load_input()
    # Iterate through the groups of numbers (problems) identified in load_input
    for idx in range(len(lines[0])):
        # Calculate the result for each problem group
        temp = calculate_line(*[lines[i][idx] for i in range(len(lines[:-1]))], operator=lines[-1][idx])
        total += temp
    print(total)

main()