# AOC 2025 - Day 8: Playground - Algorithm

Today's challenge involves concepts from **Computational Geometry** or **Graph Theory** in a 3D space, because it uses **3D coordinates** and the **Euclidean distance**.

The most common computational geometry problem that relies on sorting pairwise distances between points is the **Minimum Spanning Tree (MST)** problem, often solved using an algorithm like **Kruskal's Algorithm** or **Prim's Algorithm**.

Here's an explanation of the core concepts you'll likely need to understand to solve the challenge, along with suggestions on how to adapt your existing functions.

-----

## 🗺️ Core Concepts for 3D Geometry Challenges

### 1. 3D Coordinates and Distance

Your functions already handle the input and distance correctly:

  * **3D Points:** Each line in your input represents a point in a **3D Cartesian coordinate system** as $(x, y, z)$.
  * **Euclidean Distance:** The function `euclid_distance` calculates the straight-line distance between two points $P_1 = (x_1, y_1, z_1)$ and $P_2 = (x_2, y_2, z_2)$ using the formula:
    $$d = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}$$
    This is the **length of the edge** connecting the two points.

### 2. Minimum Spanning Tree (MST)

The **Minimum Spanning Tree** is a crucial concept in graph theory.

  * **Graph:** A graph is a set of **vertices** (or nodes) and **edges** (the connections between them). In your problem, each **point** is a **vertex**, and the connection (edge) between any two points has a **weight** equal to the **distance** you calculated.
  * **Spanning Tree:** A subset of the edges of a connected, edge-weighted graph that connects *all* the vertices together, without any cycles, and using the minimum possible total edge weight.
  * **Application:** If the challenge asks for the **minimum total distance** required to connect all points, or for a way to partition the points based on a maximum distance, an MST is usually the solution.

### 3. Kruskal's Algorithm (for MST)

Kruskal's Algorithm is a **greedy algorithm** to find the MST. It's an excellent fit because your `calculate_distances` function already performs the first step:

1.  **List all edges:** You calculate the distance (weight) for every possible pair of points (edge).
2.  **Sort all edges:** You sort these edges by weight (distance) from smallest to largest. Your `calculate_distances` does exactly this\!
3.  **Iteratively add edges:** Start with an empty set of edges. Iterate through the sorted edges and add an edge to the set *if and only if* it does not form a **cycle** with the edges already included.

-----

## 🛠️ Suggestions for Your Python Implementation

To implement Kruskal's Algorithm, you need a way to detect cycles efficiently. The standard way to do this is with a **Disjoint Set Union (DSU)** data structure, also known as **Union-Find**.

### 1. The Union-Find Data Structure

The DSU structure keeps track of elements partitioned into a number of disjoint (non-overlapping) sets. It supports two primary operations:

  * **`find(i)`:** Returns the representative (or parent) of the set that element $i$ belongs to. Two elements are in the same set if their `find()` returns the same representative.
  * **`union(i, j)`:** Merges the two sets containing elements $i$ and $j$.

**Applying DSU to Kruskal's:**

When you iterate through your sorted distances (edges):

1.  Check: If `find(point_A) == find(point_B)`, then adding this edge will create a **cycle**, so you skip it.
2.  Add: If `find(point_A) != find(point_B)`, then adding this edge is safe. You **add the distance** to your total MST weight, and call `union(point_A, point_B)` to merge the two sets of connected points.

### 2. Code Adaptation

Here's how you can structure your `main` function to integrate these concepts:

```python
# --- Union-Find Helper Functions (Need to be defined) ---
def find(parent, i):
    # Finds the set representative of element i
    # (Use path compression for efficiency)
    ...

def union(parent, rank, i, j):
    # Unites the set containing i and the set containing j
    # (Use union by rank/size for efficiency)
    ...
# --------------------------------------------------------

def main():
    # 1. Get Points and Calculate Sorted Distances (Edges)
    input = get_input()
    points = split_input(input)
    # distances is a list of (distance, index_i, index_j)
    distances = calculate_distances(points)
    
    num_points = len(points)
    # Initialize Union-Find structure
    parent = list(range(num_points))  # Each point is its own set initially
    rank = [0] * num_points           # Used for union by rank
    
    mst_weight = 0
    edges_count = 0
    
    # 2. Apply Kruskal's Algorithm
    for distance, i, j in distances:
        # Check if adding the edge (i, j) creates a cycle
        root_i = find(parent, i)
        root_j = find(parent, j)
        
        if root_i != root_j:
            # No cycle: include the edge
            mst_weight += distance
            union(parent, rank, root_i, root_j)
            edges_count += 1
            
            # Optimization: The MST for N vertices has N-1 edges
            if edges_count == num_points - 1:
                break
                
    print(f"Total Minimum Spanning Tree Weight: {mst_weight}")
```

Your next step should be to implement the efficient **`find`** and **`union`** functions for the Disjoint Set Union data structure.

---

To master these types of challenges, you need a solid understanding of the underlying graph theory algorithms.

Based on your code structure (calculating all pairwise distances and sorting them), the two most relevant concepts you need to understand are the **Minimum Spanning Tree (MST)** and **Kruskal's Algorithm**, which uses the **Union-Find (Disjoint Set Union)** data structure.

Here are some excellent YouTube videos that explain the theory behind these concepts, which will help you make progress with your Python solution:

### 🌲 Minimum Spanning Tree & Kruskal's Algorithm

Kruskal's algorithm is a greedy method that builds the MST by adding the lightest (shortest) edges first, provided they don't form a cycle.

* **Kruskal's Algorithm Visually Explained (Minimum Spanning Tree)**
    * **Channel:** Hello Byte
    * **URL:** [http://www.youtube.com/watch?v=OxfTT8slSLs](http://www.youtube.com/watch?v=OxfTT8slSLs)
    * **Why it helps:** This video is very visual and explains the concept of iterating through sorted edges and using the Union-Find logic (implicitly, if not explicitly named) to prevent cycles. It directly relates to your `calculate_distances` function.

* **How Do You Calculate a Minimum Spanning Tree?**
    * **Channel:** Spanning Tree
    * **URL:** [http://www.youtube.com/watch?v=Yldkh0aOEcg](http://www.youtube.com/watch?v=Yldkh0aOEcg)
    * **Why it helps:** A conceptual explanation that uses a story to illustrate how Kruskal's algorithm works, which can help solidify the intuition.

***

### 🔗 Union-Find (Disjoint Set Union) Data Structure

Kruskal's Algorithm requires an efficient way to check if two nodes are already connected (i.e., if adding an edge between them creates a cycle). This is where the **Union-Find** data structure comes in.

To complete your solution, you'll need to search for a video specifically on this structure to implement the cycle detection logic efficiently.

* **Search for:** `"Union-Find Disjoint Set Tutorial"`

Videos on Union-Find will explain the two essential operations for your Python code:

1.  **`find()`:** To determine which set (or component) a point belongs to.
2.  **`union()`:** To merge two sets after a new valid edge has been added.

By combining your current structure (3D points and sorted distances) with the MST theory and the Union-Find implementation, you will have the complete framework to solve the challenge!

[How Do You Calculate a Minimum Spanning Tree?](https://www.youtube.com/watch?v=Yldkh0aOEcg)
[Kruskal’s Algorithm Visually Explained (Minimum Spanning Tree)](https://www.youtube.com/watch?v=OxfTT8slSLs)
