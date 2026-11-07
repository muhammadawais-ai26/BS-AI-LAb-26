import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def astar(start, goal, h):
    frontier = [(h[start], 0, start, [start])]
    best_cost = {start: 0}
    expanded = []

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if g != best_cost[node]:
            continue

        if node == goal:
            return path, g, expanded

        expanded.append(node)

        for neighbor, cost in graph[node]:
            new_g = g + cost

            if neighbor not in best_cost or new_g < best_cost[neighbor]:
                best_cost[neighbor] = new_g
                new_f = new_g + h[neighbor]
                heapq.heappush(
                    frontier,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float("inf"), expanded


path, cost, expanded = astar("S", "G", heuristic)

print("A* Search")
print("Path:", path)
print("Cost:", cost)
print("Expanded:", expanded)
print("Expansion count:", len(expanded))

# Uniform Cost Search
zero_heuristic = {node: 0 for node in graph}
path, cost, expanded = astar("S", "G", zero_heuristic)

print("\nUniform Cost Search")
print("Path:", path)
print("Cost:", cost)
print("Expanded:", expanded)
print("Expansion count:", len(expanded))

# Overestimating heuristic experiment
overestimated = heuristic.copy()
overestimated["C"] = 10

path, cost, expanded = astar("S", "G", overestimated)

print("\nOverestimated Heuristic")
print("Path:", path)
print("Cost:", cost)
print("Expanded:", expanded)
print("Expansion count:", len(expanded))