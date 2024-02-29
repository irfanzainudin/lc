# Longest Common Prefix
# wrong
# wrong

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    stri = strs[0]
    shortest_string_length = len(stri)
    for string in strs[1:]:
        if len(string) <= shortest_string_length:
            shortest_string_length = len(string)

    commonPrefix = ''
    for string in strs[1:]:
        i = 0
        while i < shortest_string_length:
            if stri[i] != string[i]:
                commonPrefix = commonPrefix[:i]
                break
            else:
                commonPrefix += stri[i]
            i += 1

    return commonPrefix


print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["a"]))
