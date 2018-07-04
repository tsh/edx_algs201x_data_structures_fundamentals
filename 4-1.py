from math import floor

class Tree:
    def __init__(self, s):
        s = s.split('\n')
        n = int(s[0])
        s = s[1:]
        self.nodes = [None] * n
        values = [tuple(map(int, vals.split())) for vals in s]
        root, l, r = values[0]
        self.nodes[0] = root
        self.nodes[1] = ...
        for node, left, right in values[1:]:
             pass
        print(self.nodes)

    def left_child(self, pos):
        return 2*pos+1

    def right_child(self, pos):
        return 2*pos+2

    def get_parent(self, pos):
        return floor((pos-1)/2)

    def in_order(self):
        pass

    def pre_order(self):
        pass

    def post_order(self):
        pass

if __name__ == '__main__':
    s = """10
4 1 2
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
    Tree(s)