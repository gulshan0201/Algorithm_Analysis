def topologicalSortUtil(v, adj, visited, stack):
# Mark the current node as visited
    visited[v] = True
# Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)
# Push current vertex to stack which stores the result
    stack.append(v)
# Function to perform Topological Sort
def topologicalSort(adj, V):
# Stack to store the result
    stack = []
    visited = [False] * V
# Call the recursive helper function to store
# Topological Sort starting from all vertices one by
# one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)
# Print contents of stack
    print("Topological sorting of the graph:", end=" ")
    while stack:
        print(stack.pop(), end=" ")
# Number of nodes
V = 8
# Edges
edges = [[7,6], [7,5], [5,4], [5,2], [6,3], [6,4], [2,1], [3,1],[1,0]]
# Graph represented as an adjacency list
adj = [[] for _ in range(V)]
for i in edges:
    adj[i[0]].append(i[1])
topologicalSort(adj, V)
