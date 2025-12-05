items = []
ranges = []

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

def count_fresh_item_ids(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    count = 0
    curr = -1
    for start,end in ranges:
        if curr >= start:
            start = curr+1
        if start <= end:
            count += end-start+1
        curr = max(curr, end)
    
    return count


if __name__ == "__main__":
    ranges, items = get_input()
    print(count_fresh_item_ids(ranges))