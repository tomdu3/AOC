from functools import cache
in_put = "125 17"

# get input from the file
with open('input11.txt') as f:
    in_put = f.read().strip()

def get_data(in_put):
    num_list = []
    for num in in_put.split():
        num_list.append(int(num))
    
    return num_list

print(get_data(in_put))

@cache
def rearrange_stone(stone, times)
    if times = 0:
        return 1
    if stone == 0:
        return rearrange_stone(1, times - 1)
    if (length:= len(stone_str:= str(stone))) % 2 == 0:
        return rearrange_stone(int(stone_str[:len(stone_str) // 2]), times - 1) + rearrange_stone(int(stone_str[len(stone_str) // 2:]), times - 1)
    return rearrange_stone(stone * 2024, times - 1)

def blink(stones, times):
    count_stones = 0
    for stone in stones:
        count_stones += len(rearrange_stone(stone, times))
        
    return count_stones
data = get_data(in_put)
print(blink(data, 75))

