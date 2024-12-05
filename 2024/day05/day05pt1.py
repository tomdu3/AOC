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
    valid_lines = []
    for line in lines:
        invalid_line = False
        for rule in rules:
            if rule[0] in line and rule[1] in line:
                if line.index(rule[0]) > line.index(rule[1]):
                    invalid_line = True
                    continue
        if not invalid_line:
            valid_lines.append(line)
    return valid_lines

def add_middle_pages(lines):
    return sum([line[len(line)//2] for line in lines])
valid_lines = check_rules(rules, lines)

print(valid_lines)
print(add_middle_pages(valid_lines))
