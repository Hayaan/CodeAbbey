# http://www.codeabbey.com/index/task_view/array-checksum

n = int(input()); res = 0
inputTuple = tuple(map(int, input().split()))
for i in range(n):
    res += inputTuple[i]
    res *= 113
    res %= 10000007
print(res)