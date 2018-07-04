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
        print(self.nodes, self.left, self.right)


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
    Tree(s)