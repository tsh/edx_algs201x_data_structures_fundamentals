from math import floor

class Tree:
    def __init__(self, s):
        items = s.split('\n')
        self.nodes, self.left, self.right = [], [], []
        for item in items:
            n, l, r = map(int, item.split())
            self.nodes.append(n)
            self.left.append(l if l != -1 else None)
            self.right.append(r if r != -1 else None)

    def pre_order(self):
        ids = [0]
        res = []
        while ids:
            nid = ids.pop()
            node = self.nodes[nid]
            if node:
                res.append(node)
            l, r = self.left[nid], self.right[nid]
            if r:
                ids.append(r)
            if l:
                ids.append(l)
        return res

    def in_order(self):
        pass

    def post_order(self):
        pass

if __name__ == '__main__':
    s = """4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1"""

    # result:
    """
    1, 2, 3, 4, 5
    4, 2, 1, 3, 5
    1, 3, 2, 5, 4
    """
    t = Tree(s)
    print(t.in_order())
    print(t.pre_order())
    print(t.post_order())