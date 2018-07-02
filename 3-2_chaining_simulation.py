def poly_hash(string, m):
    p = 1000000007
    x = 263
    h = 0
    for s in reversed(string):
        h = (h * x + ord(s)) % p
    return h % m


def chain(commands, m):
    table = [[] for _ in range(m)]
    for line in commands.split('\n'):
        command, arg = line.split()
        hsh = poly_hash(arg, m)
        if command == 'add':
            table[hsh].insert(0, arg)
        elif command == 'check':
            lst = table[int(arg)]
            if lst:
                print(' '.join(lst))
            else:
                print()




if __name__ == '__main__':
    chain("""add check
add test
add look
add aba
add caba
check 0
check 1
add hm
check 1""", 2)