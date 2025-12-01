with open("input.txt", "r") as f:
    lines = f.readlines()
zero_count = 0
current = 50
for line in lines:
    line = line.strip()
    direction, steps = line[0], int(line[1:])
    if direction == "R":
        current += steps
    elif direction == "L":
        current -= steps
    
    if current % 100 == 0:
        zero_count += 1
print(zero_count)