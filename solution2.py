def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Example Usage:
expr = "{[()()]}"
print("Balanced" if is_balanced(expr) else "Not Balanced")
