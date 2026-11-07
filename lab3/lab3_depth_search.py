graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
    "Z": []
}


def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    if limit == 0:
        return "CUTOFF", []

    cutoff_found = False

    for next_node in graph[node]:
        if next_node not in path:
            status, result = dls(
                next_node, goal, limit - 1,
                path + [next_node]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", []

    return "FAILURE", []


def iddfs(start, goal, max_depth):
    for depth in range(1, max_depth + 1):
        status, path = dls(start, goal, depth, [start])

        print("Depth:", depth)
        print("Status:", status)
        print("Path:", path)

        if status == "FOUND":
            return path

    return []


print("DLS Results")

for limit in range(1, 5):
    status, path = dls("A", "G", limit, ["A"])
    print("Limit:", limit, "Status:", status, "Path:", path)

print("\nIDDFS Results")
iddfs("A", "G", 4)
print("\nEdge Case Test")

status, path = dls("A", "A", 0, ["A"])

print("Start = Goal")
print("Status:", status)
print("Path:", path)