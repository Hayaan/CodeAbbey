# http://www.codeabbey.com/index/task_view/weighted-sum-of-digits

n = int(input()); result = ""
inputList = input().split()
# inputList = list(map(int, inputList))
for num in inputList:
    res = 0
    for j in range(0, len(str(num))):
        res += int(str(num)[j])*(j+1)
    result += str(res) + " "
print(result.strip())
