prime = 1000000007

def find(pattern, text):
    """Rabin Karp"""
    result = []
    pattern_hash = poly_hash(pattern)
    text_hash = poly_hash(text[0:len(pattern)])
    if pattern_hash == text_hash and pattern == text[0:len(pattern)]:
        result.append(0)
    for i in range(1, len(text) - len(pattern)):
        prev_letter = text[i-1]
        next_i = i+len(pattern)-1
        text_hash = ((text_hash - ord(prev_letter)) / prime) + ord(text[next_i]) * pow(prime, len(pattern)-1)
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            result.append(i)
    return result


def poly_hash(string):
    h = 0
    for i, s in enumerate(string):
        h += ord(s) * pow(prime, i)
    return h


if __name__ == '__main__':
    print(' '.join(map(str, find('zz', 'ZzzzzZzzZzzzZzzzZZZzzzzZZzzZ'))))