# Roman to Integer
# wrong
# accepted

def romanToInt(s: str) -> int:
    count = 0
    prev_char = s[0]
    for c in s:
        if c == 'M':
            if prev_char == 'C':
                count += 800
            else:
                count += 1000
        elif c == 'D':
            if prev_char == 'C':
                count += 300
            else:
                count += 500
        elif c == 'C':
            if prev_char == 'X':
                count += 80
            else:
                count += 100
        elif c == 'L':
            if prev_char == 'X':
                count += 30
            else:
                count += 50
        elif c == 'X':
            if prev_char == 'I':
                count += 8
            else:
                count += 10
        elif c == 'V':
            if prev_char == 'I':
                count += 3
            else:
                count += 5
        elif c == 'I':
            count += 1
        prev_char = c
    return count


# print(romanToInt('XII'))
# print(romanToInt('III'))
# print(romanToInt('LVIII'))
# print(romanToInt("MCMXCIV"))
# print(romanToInt("IV"))
# print(romanToInt("XIV"))
# print(romanToInt("XVI"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("XL"))
print(romanToInt("XC"))
print(romanToInt("CD"))
print(romanToInt("CM"))
