# http://www.codeabbey.com/index/task_view/fibonacci-sequence

# input data is limited to the 1000th fibonacci value
memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        memo[n] = fibonacci(n-2) + fibonacci(n-1)
        return memo[n]

fibonacci(1000)

n = int(input()); outputString = ""
for i in range(n):
    inputVal = int(input())
    for key, val in memo.items():
        if inputVal == val:
            outputString += str(key) + " "
print(outputString.strip())