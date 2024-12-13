from pprint import pprint

in_put = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

def clean_input(in_put):
    a_buttons = []
    b_buttons = []
    prizes = []
    for line in in_put.split('\n'):
        if ':' not in line:
            continue
        data = line.split(':')[1]
        print(data)

        if "Button A:" in line:
            x = int(data.split(',')[0].replace('X+', '').strip())
            y = int(data.split(',')[1].replace('Y+', '').strip())
            print("A:", x,y)
            a_buttons.append((x,y))
        if "Button B:" in line:
            x = int(data.split(',')[0].replace('X+', '').strip())
            y = int(data.split(',')[1].replace('Y+', '').strip())
            print("B:", x,y)
            b_buttons.append((x,y))
        if "Prize:" in line:
            x = int(data.split(',')[0].replace('X=', '').strip())
            y = int(data.split(',')[1].replace('Y=', '').strip())
            print("P:", x,y)
            prizes.append((x,y))

    return a_buttons, b_buttons, prizes

def find_smallest_tokens(prize, button_a, button_b, times=101):
    button_combination = []
    for i in range(times):
        for j in range(times):
            if button_a[0]*i + button_b[0]*j == prize[0] and button_a[1]*i + button_b[1]*j == prize[1]:
                button_combination.append((i,j))
    if len(button_combination) == 0:
        return False
    return button_combination

# print(input_data[2][0], input_data[0][0], input_data[1][0])
# pprint(find_smallest_tokens(input_data[2][0], input_data[0][0], input_data[1][0]))

def calculate_tokens(input_data):
    sum_of_tokens = 0

    for combination in range(len(input_data[0])):
        print(combination)
        result = find_smallest_tokens(input_data[2][combination], input_data[0][combination], input_data[1][combination])
        if result:
            sum_of_tokens += 3 * result[0][0] + result[0][1]

        print(result)
    return sum_of_tokens

# take date from input file
in_put = open("input13.txt").read().strip()
input_data = clean_input(in_put)
tokens = calculate_tokens(input_data)
print(tokens)
