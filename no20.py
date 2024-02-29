# Valid Parentheses
# wrong
# wrong
# runtime error
# accepted

def isValid(s: str) -> bool:
    seen = []
    for c in s:
        if c is '(':
            seen.append(c)
        elif c is '[':
            seen.append(c)
        elif c is '{':
            seen.append(c)

        if c is ')':
            if len(seen) > 0 and seen[len(seen) - 1] is '(':
                seen.pop()
            else:
                return False
        elif c is ']':
            if len(seen) > 0 and seen[len(seen) - 1] is '[':
                seen.pop()
            else:
                return False
        elif c is '}':
            if len(seen) > 0 and seen[len(seen) - 1] is '{':
                seen.pop()
            else:
                return False

    if len(seen) != 0:
        return False

    return True


print(isValid('()'))
print(isValid('(())'))
print(isValid('(()'))
print(isValid('()[]'))
print(isValid('()\{\}'))
print(isValid('()\{'))
print(isValid('(]'))
print(isValid('('))
print(isValid(']'))


# FIRST ATTEMPT
# def isValid(s: str) -> bool:
#     p = 0
#     b = 0
#     c = 0
#     for i in s:
#         if i is '(':
#             p += 1
#         elif i is '[':
#             b += 1
#         elif i is '{':
#             c += 1
#         elif i is ')':
#             p -= 1
#         elif i is ']':
#             b -= 1
#         elif i is '}':
#             c -= 1
#     if p != 0 or b != 0 or c != 0:
#         return False
#     else:
#         return True
