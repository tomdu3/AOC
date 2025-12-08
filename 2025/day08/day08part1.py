def get_input():
    with open("input.txt", "r") as f:
        return f.read().splitlines()
    
def split_input(input):
    lines = []
    for line in input:
        x,y,z = line.split(",")
        lines.append((int(x), int(y), int(z)))
    return lines

def squared_euclid_distance(point1, point2):
    distance = 0
    for i in range(3):
        distance += (point1[i] - point2[i]) ** 2
    return distance


def calculate_distances(points):
    distances = []
    n = len(points)
    for i in range(n):
        for j in range(n):
            if i > j:
                distances.append((squared_euclid_distance(points[i], points[j]), i, j))
    return sorted(distances)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # Track size of each component
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If already in same component, do nothing
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def main():
    input_data = get_input()
    points = split_input(input_data)
    
    # Generate all possible connections sorted by distance
    connections = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = squared_distance(points[i], points[j])
            connections.append((dist, i, j))
    
    # Sort by distance (squared distance preserves order)
    connections.sort(key=lambda x: x[0])
    
    # Initialize DSU to track circuits
    dsu = DSU(n)
    
    last_x_product = 0
    
    # Process connections in order of increasing distance
    for dist, i, j in connections:
        # Check if these boxes are in different circuits
        if dsu.find(i) != dsu.find(j):
            # If this is the connection that will reduce circuits from 2 to 1
            if dsu.components == 2:
                # Get the X coordinates of these two boxes
                x1, x2 = points[i][0], points[j][0]
                last_x_product = x1 * x2
            
            # Connect them
            dsu.union(i, j)
        
        # Stop when all boxes are in one circuit
        if dsu.components == 1:
            break
    
    print(f"Last X product: {last_x_product}")
    
    
if __name__ == "__main__":
    main()
