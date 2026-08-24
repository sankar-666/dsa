# def valid_parentheses(s):
#     stack = []

#     for ch in s:
#         if ch in "([{":
#             stack.append(ch)
#             continue

#         if not stack:
#             return False

#         top = stack.pop()

#         if (
#             (top == "(" and ch != ")") or
#             (top == "[" and ch != "]") or
#             (top == "{" and ch != "}")
#         ):
#             return False

#     return len(stack) == 0

def valid_parentheses(s):

    stack = []

    for ch in s:
        if ch in "{([":
            stack.append(ch)
            continue

        if stack:
            top = stack.pop()

            if  (
                    (top == "(" and ch != ")") or
                    (top == "{" and ch != "}") or
                    (top == "[" and ch != "]") 
                ):
                return False


    return len(stack) == 0


print(valid_parentheses("({[]})"))