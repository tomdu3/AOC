# Solution Guide: Advent of Code 2025, Day 9

## Part 1

### Problem Summary

The goal of Part 1 is to find the largest possible rectangular area that can be formed on a grid of tiles. The only constraint is that the rectangle must use two of the "red tiles" from the input list as its opposite corners.

### Core Concept: Calculating Area on a Discrete Grid

The most common mistake, and the key insight for this puzzle, is how area is calculated. In a continuous coordinate system (like a graph in a math class), the area of a rectangle with corners at `(x1, y1)` and `(x2, y2)` is simply the absolute difference of the coordinates multiplied: `abs(x2 - x1) * abs(y2 - y1)`.

However, this problem takes place on a **grid of square tiles**. This is a discrete space, and the calculation must be inclusive of the tiles at the boundaries.

**Example:** Imagine a 1D line of tiles. A line stretching from a tile at position `x=2` to a tile at position `x=5` includes the tiles at positions 2, 3, 4, and 5. The total count of tiles is 4.
*   The continuous formula gives: `5 - 2 = 3`. (Incorrect)
*   The discrete formula gives: `(5 - 2) + 1 = 4`. (Correct)

Therefore, for a 2D rectangle, we must apply this `+ 1` logic to both the width and the height.

The correct formula for the area between corners `(x1, y1)` and `(x2, y2)` is:
**`Area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)`**

### Example Walkthrough from the Puzzle

The puzzle states that the largest rectangle has an area of 50, formed between the red tiles at `(2, 5)` and `(11, 1)`. Let's apply the correct formula:

*   **Corners:** `p1 = (2, 5)` and `p2 = (11, 1)`
*   **X-coordinates:** 2 and 11
*   **Y-coordinates:** 1 and 5
*   **Width calculation:** `abs(11 - 2) + 1 = 9 + 1 = 10` tiles.
*   **Height calculation:** `abs(5 - 1) + 1 = 4 + 1 = 5` tiles.
*   **Total Area:** `10 * 5 = 50`.

This matches the expected answer and confirms our formula is correct.

### Algorithm: A Brute-Force Approach

Because the problem asks for the largest rectangle formed by *any* two red tiles, and the number of red tiles is manageable, a simple and effective algorithm is to check every possible pair. This is known as a brute-force search.

The algorithm is as follows:
1.  Initialize a variable `max_area` to 0.
2.  Parse the input file to create a list of all red tile coordinates.
3.  Use two nested loops to create every unique pair of points from the list. For a point at index `i`, the inner loop can start at `i` to avoid checking the same pair twice.
4.  For each pair of points, calculate the area of the rectangle they form using the discrete area formula: `(abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)`.
5.  Compare this `current_area` with `max_area`. If it's larger, update `max_area`.
6.  After the loops complete, `max_area` will hold the largest possible area, which is the solution.

## Part 2

### Problem Understanding

### The Setup
- We have a set of red tiles (coordinates from input)
- When connected in order (including last to first), they form a closed polygon
- Green tiles are:
  1. All tiles on straight lines connecting consecutive red tiles (boundary)
  2. All tiles inside this closed polygon (interior)
- We need to find the largest axis-aligned rectangle where:
  - Two opposite corners are red tiles
  - **Every tile in the rectangle is either red or green** (inside the polygon)

### Key Insight
This is essentially finding the largest rectangle **completely contained within** (or on the boundary of) a simple, axis-aligned polygon, where the rectangle's opposite corners must be red tiles.

## Algorithm Approach

### Polygon Representation
The input coordinates already form the polygon vertices in order. We treat this as a closed polygon (last point connects to first).

### Point-in-Polygon Check
We need to determine if a point is inside the polygon (including its boundary). For this, we use the **Ray Casting Algorithm**:
- Shoot a ray from the point to the right (positive x-direction)
- Count how many polygon edges it crosses
- If odd: inside, if even: outside
- Special handling for points exactly on edges/vertices

### Rectangle Validation
For a rectangle defined by two red corner tiles (x1,y1) and (x2,y2), we need to check if **all points** in the rectangle are inside the polygon.

**Naive approach**: Check every point in the rectangle - too slow!

**Optimized approach**: For axis-aligned rectangles in axis-aligned polygons, we can check:
- All four corners
- Midpoints of all four edges
- Center point

This 9-point check is sufficient because:
1. If all corners are inside, the rectangle's boundary doesn't cross outside
2. The midpoints and center help detect if the rectangle straddles a "hole" or indentation
3. For convex polygons, checking corners would be enough
4. For our specific polygons (formed by connecting red tiles), this heuristic works well

### Area Calculation
Area = (|x2 - x1| + 1) × (|y2 - y1| + 1)  
We add 1 because corners are inclusive.

### Optimization Strategy
- Precompute the polygon edges once
- For each pair of red tiles (O(n²) pairs):
  - Check if rectangle is valid using 9-point test (O(1) per point, O(9n) = O(n) with constant)
  - Calculate area if valid
  - Track maximum

Total complexity: O(n³) in worst case, but with small constant factor.

## Implementation Details

### Code Structure
```python
def is_point_inside_polygon(x, y, polygon):
    # Ray casting algorithm implementation
    # Returns True if point is inside or on boundary

def rectangle_is_valid(rect_corners, polygon):
    # Check 9 key points in the rectangle
    # Returns True if all are inside polygon

def find_greatest_area_part2(coordinates):
    # Main algorithm: try all red tile pairs
    # Return maximum valid rectangle area
```

### Why This Works for the Problem
1. **Input constraints**: The polygon is axis-aligned (all edges horizontal/vertical)
2. **Red tile positions**: Corners must be red tiles, limiting candidate rectangles
3. **Polygon simplicity**: No self-intersections, closed loop
4. **Performance**: For ~2000 red tiles, O(n³) with small constant is acceptable in practice

### Example Walkthrough
For the example input with 8 points:
- There are 8×7/2 = 28 candidate rectangles
- For rectangle (2,3) to (9,5):
  - Check 9 points: all are inside polygon
  - Area = (9-2+1) × (5-3+1) = 8×3 = 24 ✓
- For rectangle (2,5) to (11,1):
  - Some points fail the 9-point test
  - Rectangle extends outside polygon ✗

## Potential Improvements
If this is too slow for the actual input:
1. **Coordinate compression**: Build a grid of unique x/y values
2. **Precompute inside/outside for grid cells**
3. **Use prefix sums** to quickly check if rectangle regions are entirely inside
4. **Parallel processing**: Check pairs independently

## Alternative Approaches Considered
1. **Full grid check**: Too memory-intensive (coordinates can be large)
2. **Edge intersection checking**: Complex to implement correctly
3. **Polygon rasterization**: Convert to grid, then check rectangles

## Conclusion
The 9-point check provides a good balance between correctness and performance for this specific problem structure. It leverages the axis-aligned nature of both the polygon and the rectangles we're checking.