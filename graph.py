def dfs(graph, start):
    visited = set()
    finished = set()

    def visit(node):
        print(f"\033[93mVisited: {node}")
        visited.add(node)

    def finish(node):
        print(f"\033[92mFinished: {node}")
        finished.add(node)

    def dfs_recursive(node):
        visit(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)
        finish(node)

    dfs_recursive(start)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')