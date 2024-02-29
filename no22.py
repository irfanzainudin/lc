# Generate Parentheses
# Given n pairs of parentheses, write a function to
# generate all combinations of well-formed parentheses.
#

n = int(input().strip())

if n == 0 or n > 8:
    exit(0)
