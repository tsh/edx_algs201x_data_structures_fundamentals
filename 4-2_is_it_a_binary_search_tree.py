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
        if nmin > val or nmax < val:
            return False
        return go(left[nodei], nmin, val) and go(right[nodei], val, nmax)

    return go(0, float('-Inf'), float('Inf'))

if __name__ == '__main__':
    s = """4 1 -1
2 2 3
1 -1 -1
5 -1 -1"""  # INCORRECT
    print(is_bst(s))

    print(is_bst("""-735041448 1 16
-832108451 2 9
-1045319940 3 6
-1397855278 4 5
-1596566483 -1 -1
-1389882406 -1 -1
-948839464 7 8
-1012320116 -1 -1
-897977144 -1 -1
-813481023 10 13
-824163522 11 12
-827870431 -1 -1
-817165058 -1 -1
-740772260 14 15
-760226374 -1 -1
-737383456 -1 -1
-347180881 17 24
-693180272 18 21
-722121977 19 20
-734146581 -1 -1
-697899130 -1 -1
-645252057 22 23
-670690567 -1 -1
-642947751 -1 -1
2096833725 25 28
1912879271 26 27
1233091160 -1 -1
1980569275 -1 -1
2110822766 29 30
2101212694 -1 -1
2146730371 -1 -1"""))