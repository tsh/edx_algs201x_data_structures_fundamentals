def phone_book(s):
    book = [None] * 10**7
    for line in s.split('\n'):
        query = line.split()
        if query[0] == 'find':
            val = book[int(query[1])]
            if val:
                print(val)
            else:
                print('not found')
        elif query[0] == 'add':
            book[int(query[1])] = query[2]
        elif query[0] == 'del':
            book[int(query[1])] = None

if __name__ == '__main__':
    s = """add 9999999 bigNum
find 9999999
add 9999998 notSoBig
del 9999998
find 9999998
add 1 aaaaaaaaaaaaaaa
add 2 testForLen
find 2
find 1"""
    phone_book(s)