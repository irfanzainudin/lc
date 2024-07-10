# Longest Common Prefix
# wrong
# wrong
# looked at solutions

from typing import List


# def longestCommonPrefix(strs: List[str]) -> str:
def longestCommonPrefix(v: List[str]) -> str:
    # if len(strs) == 1:
    #     return strs[0]

    # stri = strs[0]
    # shortest_string_length = len(stri)
    # for string in strs[1:]:
    #     if len(string) <= shortest_string_length:
    #         shortest_string_length = len(string)

    # commonPrefix = ''
    # for string in strs[1:]:
    #     i = 0
    #     while i < shortest_string_length:
    #         if stri[i] != string[i]:
    #             commonPrefix = commonPrefix[:i]
    #             break
    #         else:
    #             commonPrefix += stri[i]
    #         i += 1

    # return commonPrefix

    # Looked at solution:
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans 


print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['flower', 'flower', 'flower']))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["a"]))
