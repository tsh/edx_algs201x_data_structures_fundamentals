def is_bst(s):
    items = s.split('\n')
    nodes, left, right = [], [], []
    for item in items:
        n, l, r = map(int, item.split())
        nodes.append(n)
        left.append(l if l != -1 else None)
        right.append(r if r != -1 else None)

    def go(nodei, nmin, nmax):
        if nodei is None:
            return True
        val = nodes[nodei]
        if nmin > val or nmax <= val:
            return False
        return go(left[nodei], nmin, val) and go(right[nodei], val, nmax)

    return go(0, float('-Inf'), float('Inf'))

if __name__ == '__main__':
    print(is_bst("""2 1 2
1 -1 -1
2 -1 -1""")) # CORRECT

    print(is_bst("""2 1 2
2 -1 -1
3 -1 -1"""))  # INCORRECT

    print(is_bst("""-1388983464 -1 1
-1388983464 -1 2
-1388983464 -1 3
-1388983464 -1 4
-1388983464 -1 5
-1388983464 -1 6
-1388983464 -1 7
-1388983464 -1 8
-1388983464 -1 9
-1388983464 -1 -1"""))