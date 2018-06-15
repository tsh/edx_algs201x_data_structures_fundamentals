# python3

from collections import defaultdict


def compute_height(parents):
    # build tree
    tree = defaultdict(list)
    for node, parent in enumerate(parents):
        tree[parent].append(node)

    queue = tree[-1]
    height = 0
    while queue:
        nodes_count = len(queue)
        height += 1
        while nodes_count > 0:
            node = queue.pop(0)
            children = tree[node]
            if children:
                queue.extend(children)
            nodes_count -= 1
    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
