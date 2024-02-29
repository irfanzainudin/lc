def fizzBuzz(n: int):
    answer = []
    for num in range(1, n+1):
        print(num)
        div3 = num % 3 == 0
        div5 = num % 5 == 0

        if div3 and div5:
            answer.append("FizzBuzz")
        elif div3:
            answer.append("Fizz")
        elif div5:
            answer.append("Buzz")
        else:
            answer.append(num)
    print(answer)
    return answer


fizzBuzz(3)
