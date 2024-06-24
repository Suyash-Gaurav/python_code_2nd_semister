class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set with each vertex as its own parent and rank 0.

        Args:
            vertices (list): List of vertices in the graph.
        """
        self.parent = {}
        for v in vertices:
            self.parent[v] = v  # Each vertex is its own parent initially
        self.rank = {v: 0 for v in vertices}  # Rank is initialized to 0 for all vertices

    def find(self, v):
        """
        Find the root of the set containing vertex v, with path compression.

        Args:
            v: The vertex to find.

        Returns:
            The root of the set containing v.
        """
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, v1, v2):
        """
        Union the sets containing v1 and v2.

        Args:
            v1: Vertex in the first set.
            v2: Vertex in the second set.
        """
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(adj_matrix):
    """
    Perform Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Args:
        adj_matrix (list): Adjacency matrix representing the graph.

    Returns:
        list: Adjacency matrix representing the MST.
    """
    num_vertices = len(adj_matrix)
    vertices = list(range(num_vertices))

    # Create a list of edges with their weights
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))

    # Sort edges based on their weights
    edges.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(vertices)
    mst = []  # List to store edges of the MST

    for edge in edges:
        u, v, weight = edge
        root_u = disjoint_set.find(u)
        root_v = disjoint_set.find(v)

        if root_u != root_v:
            mst.append(edge)
            disjoint_set.union(root_u, root_v)

    # Create the adjacency matrix for the MST
    mst_adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v, weight in mst:
        mst_adj_matrix[u][v] = weight
        mst_adj_matrix[v][u] = weight

    return mst_adj_matrix


# Example usage:
if __name__ == "__main__":
    # Example adjacency matrix
    adjacency_matrix = [
        [0, 2, 3, 0, 0],
        [2, 0, 15, 2, 0],
        [3, 15, 0, 0, 13],
        [0, 2, 0, 0, 9],
        [0, 0, 13, 9, 0]
    ]

    minimal_spanning_tree = kruskal(adjacency_matrix)

    print("Adjacency matrix of minimal spanning tree:")
    for row in minimal_spanning_tree:
        print(row)
