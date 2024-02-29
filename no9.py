# Palindrome
# accepted

def isPalindrome(x: int) -> bool:
    xstr = str(x)
    if len(xstr) == 1:
        return True
    i = 0
    j = len(xstr)
    for c in xstr:
        if c != xstr[j - 1]:
            return False
        j -= 1
    return True


uinput = input()
print(isPalindrome(x=uinput))
