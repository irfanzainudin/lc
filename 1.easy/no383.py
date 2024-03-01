def canConstruct(ransomNote: str, magazine: str) -> bool:
    d = {}
    for c in magazine:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in ransomNote:
        if c in d and d[c] is 0:
            return False
        else:
            d[c] -= 1
    return True


print(canConstruct("aa", "aab"))
print(canConstruct("aa", "ab"))
