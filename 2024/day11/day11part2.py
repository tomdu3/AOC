from functools import cache  # memoization with cache

with open('input11.txt') as f:
    in_put = f.read().strip()
stones = [int(x) for x in in_put.split()]

@cache
def count_stones(stone, times):
    if times == 0:
        return 1
    if stone == 0:
        return count_stones(1, times -1)
    if len(stone_str := str(stone)) % 2 == 0:
        left = int(stone_str[:len(stone_str)//2])
        right = int(stone_str[len(stone_str)//2:])
        return count_stones(left, times - 1) + count_stones(right, times - 1)
    return count_stones(stone * 2024, times - 1)

total = 0
for stone in stones:
    print(count := count_stones(stone, 75))
    total += count

print(total)

