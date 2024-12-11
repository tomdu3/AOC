in_put = "125 17"

# get input from the file
with open('input11.txt') as f:
    in_put = f.read().strip()

def get_data(in_put):
    num_list = []
    for num in in_put.split():
        num_list.append(num)
    
    return num_list

print(get_data(in_put))

def rearrange_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            add_two_stones = [stone[:len(stone) // 2], str(int(stone[len(stone) // 2:]))]
            new_stones.extend(add_two_stones)
        else:
            new_stone = int(stone) * 2024
            new_stones.append(str(new_stone))
    return new_stones

def blink(stones, times):
    arrangement = stones
    for i in range(times):
        arrangement = rearrange_stones(arrangement)
    return arrangement

print(len(blink(get_data(in_put), 25)))

