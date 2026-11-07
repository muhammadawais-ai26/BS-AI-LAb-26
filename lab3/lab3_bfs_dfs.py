from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = deque([start])
    visited = []
    parent = {start: None}

    while queue:
        current = queue.popleft()
        visited.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    path = []
    node = goal

    if node not in parent:
        return [], visited

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, visited


def dfs(start, goal):
    stack = [start]
    visited = []
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            break

        for neighbor in reversed(graph[current]):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    path = []
    node = goal

    if node not in visited:
        return [], visited

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, visited


bfs_path, bfs_order = bfs("A", "G")
dfs_path, dfs_order = dfs("A", "G")

print("BFS Path:", bfs_path)
print("BFS Visit Order:", bfs_order)

print("DFS Path:", dfs_path)
print("DFS Visit Order:", dfs_order)