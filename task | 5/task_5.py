import matplotlib.pyplot as plt
import networkx as nx
import uuid


class Node:
    def __init__(self, key, color="red"):
        self.left = None
        self.right = None
        self.value = key
        self.base_color = color
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


def dfs(node, visited, color):
    if node is not None:
        visited.add(node.id)
        node.color = get_color(color, len(visited))
        dfs(node.left, visited, color)
        dfs(node.right, visited, color)


def bfs(root, color):
    if root is not None:
        visited = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                node.color = get_color(color, len(visited))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


def get_color(color, index):
    base_rgb = tuple(int(color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    step = 15
    new_rgb = tuple(min(255, c + index * step) for c in base_rgb)
    return "#{:02X}{:02X}{:02X}".format(*new_rgb)


def main():
    root = Node(0)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(11)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.right.left.left = Node(10)
    root.right.left.right = Node(14)

    draw(root)

    dfs(root, set(), root.base_color)
    draw(root)

    bfs(root, root.base_color)
    draw(root)


if __name__ == "__main__":
    main()