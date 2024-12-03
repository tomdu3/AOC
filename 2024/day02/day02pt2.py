# in_put = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

# in_put = in_put.split('\n')

with open('input2.txt') as f:
    in_put = f.readlines()

def check_report(report: list, second_check=False):
    diff = [report[i]-report[i-1] for i in range(1,len(report))]
    print(report, diff)
    if 0 in diff or abs(min(diff)) > 3 or max(diff) > 3:
       return False
    if diff[0] < 0:
        check = -1
    else:
        check = 1
    for i in range(len(diff)):
        if diff[i]//abs(diff[i]) != check:
            return False
    return True

def second_check(report: list):
    if check_report(report):
        return True
    for i in range(len(report)):
        new_report = report[::]
        new_report.pop(i)
        if check_report(new_report):
            return True
    return False

num_of_safe = 0
for line in in_put:
    line = [int(el) for el in line.split()]
    safe = second_check(line)
    if safe:
        num_of_safe += 1
print(num_of_safe)
