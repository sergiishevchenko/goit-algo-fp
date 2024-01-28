import heapq

import networkx as nx


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not bool(self.queue)

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)


def dijkstra_alg(graph, start_node):
    visited = set()

    distances = {
        node: float("infinity") for node in graph.nodes
    }

    distances[start_node] = 0
    queue = Queue()
    queue.enqueue(start_node, 0)

    while not queue.is_empty():
        current_distance, current_node = queue.dequeue()

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.enqueue(neighbor, distance)

    return distances


def main():
    graph = nx.Graph()

    graph.add_edge("A", "B", weight=1)
    graph.add_edge("B", "C", weight=2)
    graph.add_edge("A", "C", weight=5)
    graph.add_edge("C", "D", weight=1)
    graph.add_edge("A", "D", weight=8)

    distances = dijkstra_alg(graph, "A")

    for node, distance in distances.items():
        print(f"Shortest distance from {node}: {distance}")


if __name__ == "__main__":
    main()
