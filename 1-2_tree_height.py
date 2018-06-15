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
    # n = int(input())
    # parents = list(map(int, input().split()))
    parents = [-1, 0, 4, 0, 3]
    print(compute_height(parents))  # 4

main()
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()