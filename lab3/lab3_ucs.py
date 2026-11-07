import heapq

graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 2), ("G", 7)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = [(start, [start])]
    visited = []

    while queue:
        node, path = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []


def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []
    processed = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in processed:
            continue

        processed.add(node)
        visited.append(node)

        if node == goal:
            return path, cost, visited

        for neighbor, weight in graph[node]:
            if neighbor not in processed:
                heapq.heappush(
                    queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return [], 0, visited


def path_cost(path):
    total = 0

    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i + 1]:
                total += weight
                break

    return total


bfs_path = bfs("A", "G")
ucs_path, ucs_cost, order = ucs("A", "G")

print("BFS Path:", bfs_path)
print("BFS Total Cost:", path_cost(bfs_path))

print("\nUCS Path:", ucs_path)
print("UCS Total Cost:", ucs_cost)
print("UCS Processing Order:", order)

print("Verified Cost:", path_cost(ucs_path))