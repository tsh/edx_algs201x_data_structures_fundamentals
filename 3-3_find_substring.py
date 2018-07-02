prime = 1000000007

def find(pattern, text):
    """Rabin Karp"""
    result = []
    pattern_hash = poly_hash(pattern)
    text_hash = poly_hash(text[0:len(pattern)])
    if pattern_hash == text_hash and pattern == text[0:len(pattern)]:
        result.append(0)
    return result


def poly_hash(string):
    h = 0
    for i, s in enumerate(string):
        h += ord(s) * pow(prime, i)
    return h



if __name__ == '__main__':
    print(find('zz', 'ZzzzzZzzZzzzZzzzZZZzzzzZZzzZ'))