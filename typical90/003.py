from collections import defaultdict

N = int(input())

graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distances = defaultdict(int)
distances[1] = 0

nodes = set()
nodes.add(1)
last_node = 1
while len(distances) != N:
    next_nodes = set()
    for node in nodes:
        for next_node in graph[node]:
            if next_node not in distances:
                distances[next_node] = distances[node] + 1
                next_nodes.add(next_node)
                last_node = next_node
    nodes = next_nodes

distances = defaultdict(int)
distances[last_node] = 0
nodes = set()
nodes.add(last_node)
while len(distances) != N:
    next_nodes = set()
    for node in nodes:
        for next_node in graph[node]:
            if next_node not in distances:
                distances[next_node] = distances[node] + 1
                next_nodes.add(next_node)
                last_node = next_node
    nodes = next_nodes

print(max(distances.values()) + 1)
