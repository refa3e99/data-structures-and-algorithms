def validate_brackets(string):
    stack = []
    expr = ''
    for i in string:
        if i in "(){}[]":
            expr += i

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)

        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True


# print(validate_brackets('(){}[[]]'))