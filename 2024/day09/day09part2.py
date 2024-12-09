in_put = "2333133121414131402"

# Read input from the file
with open('input09.txt') as f:
    in_put = f.read().strip()

def make_disk(in_put):
    files = {}
    blanks = []

    id = 0
    pos = 0
    for index, ch in enumerate(in_put):
        repeat = int(ch)
        if index % 2 == 0:
            files[id] = (pos, repeat) 
            id += 1
        else:
            if repeat != 0:
                blanks.append((pos, repeat))
        pos += repeat
    return files, blanks

def move_files(files, blanks):
    id = len(files)
    while id > 0:
        id -= 1
        pos, size = files[id]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[id] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break
    return files

def sum_of_files(files):
    final_sum = 0
    for id in files:
        for index in range(files[id][0], files[id][0]+files[id][1]):
            final_sum += index * id
    return final_sum
disk = make_disk(in_put)
rearranged = move_files(disk[0], disk[1])
print(sum_of_files(rearranged))


