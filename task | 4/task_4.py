import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid

from copy import copy

from consts import SET


class Node:
    def __init__(self, key, color="red"):
        self.left = None
        self.right = None
        self.value = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, position, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            position[node.left.id] = (l, y-1)
            l = add_edges(graph, node.left, position, x=l, y=y-1, layer=layer+1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            position[node.right.id] = (r, y-1)
            r = add_edges(graph, node.right, position, x=r, y=y-1, layer=layer+1)

    return graph


def draw(root):
    tree = nx.DiGraph()

    position = {root.id: (0, 0)}
    tree = add_edges(tree, root, position)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    nx.draw(tree, pos=position, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap(heap, index=0):
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap(heap, 2 * index + 1)
        node.right = build_heap(heap, 2 * index + 2)
        return node
    return None


def draw_heap(nodes):
    heap = copy(nodes)
    heapq.heapify(heap)
    nodes = build_heap(heap)
    draw(nodes)


if __name__ == "__main__":
    draw_heap(SET)