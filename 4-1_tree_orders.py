from itertools import chain


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
        while ids:
            nid = ids.pop()
            node = self.nodes[nid]
            if node:
                yield node
            l, r = self.left[nid], self.right[nid]
            if r:
                ids.append(r)
            if l:
                ids.append(l)

    def recur_in_order(self):
        def go(id_):
            l, r = [], []
            if self.left[id_]:
                l = go(self.left[id_])
            n = [self.nodes[id_]]
            if self.right[id_]:
                r = go(self.right[id_])
            return l+n+r
        return go(0)

    def in_order(self):
        nid = 0
        s = []
        while s or nid is not None:
            if nid is not None:
                s.append(nid)
                nid = self.left[nid]
            else:
                nid = s.pop()
                yield self.nodes[nid]
                nid = self.right[nid]

    def post_order(self):
        s = [0]
        res = []
        while s:
            nid = s.pop()
            res.append(self.nodes[nid])
            if self.left[nid]:
                s.append(self.left[nid])
            if self.right[nid]:
                s.append(self.right[nid])
        return res[::-1]


def printer(ino, pre, post):
    print(' '.join(map(str, [x for x in ino]+[x for x in pre]+[x for x in post])))


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
    print([x for x in t.in_order()])
    print([x for x in t.pre_order()])
    print([x for x in t.post_order()])

    t2 = Tree("""782521203 4 -1
839950857 -1 -1
248660666 3 -1
696374696 -1 -1
971981286 1 2""")
    printer(t2.in_order(), t2.pre_order(), t2.post_order())