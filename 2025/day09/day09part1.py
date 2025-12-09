# Day 9 Part 1 of 2025 AOC

def get_input():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f]

def parse_input(input):
    return [list(map(int, line.split(","))) for line in input]

def rectangle_area(coordinates):
    """
    Given the list of two coordinates, calculate the area of the rectangle
    where the two coordinates make up two opposite corners of the rectangle.
    The area is inclusive of the tiles at the corners.
    """
    return (abs(coordinates[1][0] - coordinates[0][0]) + 1) * (abs(coordinates[1][1] - coordinates[0][1]) + 1)

def find_greatest_area(coordinates):
    """
    Given the list of coordinates, find the greatest area of a rectangle
    where the two coordinates make up two opposite corners of the rectangle.
    """
    greatest_area = 0
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i == j:
                continue
            greatest_area = max(greatest_area, rectangle_area([coordinates[i], coordinates[j]]))
    return greatest_area

def main():
    print(find_greatest_area(parse_input(get_input())))


if __name__ == "__main__":
    main()
