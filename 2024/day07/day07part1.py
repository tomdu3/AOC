import itertools


in_put = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open('input07.txt') as f:
    in_put = f.read()

def clean_input(input):
    output = {}
    for line in input.split('\n'):
        if not line:
            continue
        key = int(line.split(':')[0])
        output[key] = []
        for num in line.split(':')[1].split():
            output[key].append(int(num))
    return output

in_put = clean_input(in_put)

def check_operations(report):
    valid_operations = []
    for key in report.keys():
        list_of_combinations = list(itertools.product([0,1], repeat=len(report[key])-1))
        for combination in list_of_combinations:
            calculation = report[key][0]
            for i in range(len(combination)):
                if combination[i] == 0:
                    calculation *= report[key][i+1]
                else:
                    calculation += report[key][i+1]
            if calculation == key and key not in valid_operations:
                valid_operations.append(calculation)
    return sum(valid_operations)

print(check_operations(in_put))
