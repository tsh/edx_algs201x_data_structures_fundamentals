def merge():
    pass

if __name__ == '__main__':
    inp = \
"""5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3"""
    data = inp.split('\n')
    num_tables, _ = data[0].split()
    operations = []
    for op in data[2:]:
        dest, src = map(int, op.split())
        operations.append((dest, src))
    print(operations)

