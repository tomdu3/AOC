# in_put = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

with open("./input05.txt") as f:
    in_put = f.read()

def clean_input(in_put):
    rules, lines = [], []
    go_to_lines = False
    for line in in_put.split('\n'):
        if not line:
            go_to_lines = True
            continue

        if go_to_lines:
            lines.append([int(num) for num in line.split(',')])
        else:
            rules.append([int(num) for num in line.split('|')])

    return rules, lines
rules, lines = clean_input(in_put)

def check_rules(rules, lines):
    invalid_lines = []
    for line in lines[:]:
        invalid_line = False
        for rule in rules:
            if rule[0] in line and rule[1] in line:
                num1_index = line.index(rule[0])
                num2_index = line.index(rule[1])
                if num1_index > num2_index:
                    invalid_line = True
                    continue
        if invalid_line:
            invalid_lines.append(line)
    return invalid_lines[:]

def check_rules_and_reorder(rules, lines):
    reordered_lines = []
    for line in lines:
        ordered = False
        while not ordered:
            ordered = True
            for rule in rules:
                if rule[0] in line and rule[1] in line:
                    num1_index = line.index(rule[0])
                    num2_index = line.index(rule[1])
                    if num1_index > num2_index:
                        # Swap and mark as not ordered
                        line.pop(num2_index)
                        line.insert(num1_index, rule[1])
                        ordered = False
        reordered_lines.append(line)
    return reordered_lines[:]

def add_middle_pages(lines):
    return sum([line[len(line)//2] for line in lines])

invalid = check_rules(rules, lines)
reordered = check_rules_and_reorder(rules, invalid[:])
print(add_middle_pages(reordered))
