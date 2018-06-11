from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text, start=1):
        if char in "([{":
            stack.append((char, i))

        if char in ")]}":
            if len(stack) == 0:
                return i
            top = stack.pop()[0]
            if (char == ')' and top != '(') or\
                (char == ']' and top != '[') or\
                (char == '}' and top != '{'):
                return i
    return stack.pop()[1] if len(stack) > 0 else 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    print(find_mismatch('[]'))  # Success
    print(find_mismatch('{}[]'))  # Success
    print(find_mismatch('{[}'))  # 3
    print(find_mismatch('[](()'))  # 3

