def is_bst(s):
    items = s.split('\n')
    nodes, left, right = [], [], []
    for item in items:
        n, l, r = map(int, item.split())
        nodes.append(n)
        left.append(l if l != -1 else None)
        right.append(r if r != -1 else None)

    def go(rooti, nmin, nmax):
        pass

    return go(0, float('-Inf'), float('Inf'))

if __name__ == '__main__':
    s = """4 1 -1
2 2 3
1 -1 -1
5 -1 -1"""
    print('CORRECT' if is_bst(s) else 'INCORRECT')