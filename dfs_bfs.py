# Using a Python dictionary to act as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
visited = []  # list to keep track of visited nodes of graph.


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
visited2 = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited2, graph, node):  # function for BFS
    visited2.append(node)
