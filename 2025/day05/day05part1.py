ranges = []
items = []

def get_input():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        if len(line) == 0:
            idx += 1
            continue
        if "-" in line:
            start, end = [int(x) for x in line.split("-")]
            ranges.append([start, end])
        else:
            items.append(int(line))
        idx += 1
    return ranges, items

def count_fresh_items(ranges, items):
    fresh_count = 0
    for item in items:
        for range in ranges:
            if item >= range[0] and item <= range[1]:
                fresh_count += 1
                break
    return fresh_count


if __name__ == "__main__":
    ranges, items = get_input()
    print(count_fresh_items(ranges, items))