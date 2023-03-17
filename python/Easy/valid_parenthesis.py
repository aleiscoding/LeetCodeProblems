def isValid(s: str) -> bool:
    stack = []

    for char in s:
        if char not in ')]}':
            stack.append(char)
        elif stack:
            x = stack.pop()
            if (x == '(' and char != ')') or (x == '[' and char != ']') or (x == '{' and char != '}'):
                return False
        else:
            return False
    return False if stack else True
