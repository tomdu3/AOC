def get_input():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.read().splitlines()]
    return lines

def detect_split(lines):
    beams = set()
    len_y = len(lines)
    len_x = len(lines[0])
    split_count = 0
    for i in range(len_y):
        for j in range(len_x):
            if lines[i][j] == "S":
                beams.add((i, j))
                break
 
    for y in range(1, len_y):
       new_beams = set()
       for i, j in beams:
          if y+1 >= len_y:
            continue
          if lines[y+1][j] == "^":
            new_beams.add((y+1, j-1))
            new_beams.add((y+1, j+1))
            split_count += 1
          else:
            new_beams.add((y+1, j))
       beams = new_beams

    return split_count

def main():
    lines = get_input()
    print(detect_split(lines))

if __name__ == "__main__":
    main()