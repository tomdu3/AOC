in_put = "2333133121414131402"


# Read input from the file
with open('input09.txt') as f:
    in_put = f.read().strip()

def make_disk(in_put):
    id = 0
    disk = []
    for index, ch in enumerate(in_put):
        repeat = int(ch)
        if index % 2 == 0:
            disk += [id] * repeat
            id += 1
        else:
            disk += [-1] * repeat
    return disk

def rearrange(in_put):
    blanks = [index for index, value in enumerate(in_put) if value == -1]
    for index in blanks:
        while in_put[-1] == -1:
            in_put.pop()
        if len(in_put) <= index:
            break
        in_put[index] = in_put.pop()
    return in_put

def check_sum(disk):
    sum_of_files = 0
    for i in range(len(disk)):
        sum_of_files += disk[i]*i
    return sum_of_files

disk = make_disk(in_put)
rearranged = rearrange(disk)
print(rearranged)
print(check_sum(rearranged))

