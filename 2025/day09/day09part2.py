# Day 9 Part 2 of 2025 AOC

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

def create_grid_mask(polygon):
    """
    Create a 2D grid mask where True indicates the point is inside the polygon.
    We need to handle potentially large coordinates, so we compress them.
    """
    # Extract all x and y coordinates
    all_x = sorted({x for x, _ in polygon})
    all_y = sorted({y for _, y in polygon})
    
    # Create coordinate mapping
    x_to_idx = {x: i for i, x in enumerate(all_x)}
    y_to_idx = {y: i for i, y in enumerate(all_y)}
    
    width = len(all_x)
    height = len(all_y)
    
    # Initialize grid with False
    grid = [[False] * width for _ in range(height)]
    
    n = len(polygon)
    
    # Fill the grid using ray casting algorithm
    for i in range(height):
        y = all_y[i]
        for j in range(width):
            x = all_x[j]
            
            # Check if point is exactly on the polygon boundary
            on_boundary = False
            for k in range(n):
                x1, y1 = polygon[k]
                x2, y2 = polygon[(k + 1) % n]
                
                # Check if point is on the line segment
                if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2):
                    on_boundary = True
                    break
                if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
                    on_boundary = True
                    break
            
            if on_boundary:
                grid[i][j] = True
                continue
                
            # Ray casting algorithm
            inside = False
            for k in range(n):
                x1, y1 = polygon[k]
                x2, y2 = polygon[(k + 1) % n]
                
                # Check if ray crosses edge
                if ((y1 > y) != (y2 > y)):  # Edge crosses horizontal line at y
                    # Compute x-coordinate of intersection
                    x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    if x_intersect > x:
                        inside = not inside
            
            grid[i][j] = inside
    
    return grid, x_to_idx, y_to_idx, all_x, all_y

def rectangle_is_valid(grid, x_to_idx, y_to_idx, all_x, all_y, rect_corners):
    """
    Fast check if all points in rectangle are inside polygon using precomputed grid.
    """
    x1, y1 = rect_corners[0]
    x2, y2 = rect_corners[1]
    
    # Get rectangle bounds
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    # Find indices in compressed coordinates
    # We need all x/y values between min and max to be present in our grid
    # Get indices for the rectangle corners
    if min_x not in x_to_idx or max_x not in x_to_idx:
        return False
    if min_y not in y_to_idx or max_y not in y_to_idx:
        return False
    
    idx_min_x = x_to_idx[min_x]
    idx_max_x = x_to_idx[max_x]
    idx_min_y = y_to_idx[min_y]
    idx_max_y = y_to_idx[max_y]
    
    # Check if all intermediate coordinates exist in our compressed grid
    # We need to check all x and y values in the original rectangle
    # Since we compressed, we need to ensure no "gaps" in the rectangle
    
    # Get all x and y values in the rectangle range that exist in our grid
    rect_x_indices = [i for i, x in enumerate(all_x) if min_x <= x <= max_x]
    rect_y_indices = [i for i, y in enumerate(all_y) if min_y <= y <= max_y]
    
    # Check if we have all needed coordinates
    # We need to ensure the rectangle doesn't skip any coordinates
    # If there are missing coordinates between min and max, we can't guarantee the rectangle is valid
    
    # Check every point in the rectangle (in compressed coordinates)
    for i in rect_x_indices:
        for j in rect_y_indices:
            if not grid[j][i]:  # Note: grid[y][x] indexing
                return False
    
    return True

def find_greatest_area_part2(coordinates):
    """
    Find the greatest area of a rectangle where:
    1. Two opposite corners are red tiles
    2. All tiles in rectangle are either red or green (inside the polygon)
    """
    polygon = [(x, y) for x, y in coordinates]
    
    # Create grid mask
    grid, x_to_idx, y_to_idx, all_x, all_y = create_grid_mask(polygon)
    
    greatest_area = 0
    n = len(polygon)
    
    # Check all pairs of red tiles
    for i in range(n):
        x1, y1 = polygon[i]
        # Only check tiles that exist in our compressed grid
        if x1 not in x_to_idx or y1 not in y_to_idx:
            continue
            
        for j in range(i + 1, n):
            x2, y2 = polygon[j]
            if x2 not in x_to_idx or y2 not in y_to_idx:
                continue
                
            rect_corners = [(x1, y1), (x2, y2)]
            
            # Fast check using precomputed grid
            if rectangle_is_valid(grid, x_to_idx, y_to_idx, all_x, all_y, rect_corners):
                area = rectangle_area(rect_corners)
                if area > greatest_area:
                    greatest_area = area
    
    return greatest_area

def main():
    coordinates = parse_input(get_input())
    print(find_greatest_area_part2(coordinates))

if __name__ == "__main__":
    main()