# http://www.codeabbey.com/index/task_view/rounding

n = int(input()); outputString = ""; res = 0
for i in range(n):
    num, divisor = map(int, input().split())
    res = ((num/divisor)%1)*10
    if res >= 5:    res = (num//divisor)+1
    else:           res = (num//divisor)
    outputString += str(res) + " "
print(outputString.strip())