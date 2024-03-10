arr = [1, 0, 2, 3, 0, 4, 5, 0]

j = len(arr) - 1
while j > 0:
    arr[j] = arr[j-1]
    j -= 1
arr[0] = 100

print(arr)
