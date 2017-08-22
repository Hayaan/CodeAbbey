# http://www.codeabbey.com/index/task_view/linear-function

n = int(input()); outputString = ""
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    a = (y2-y1)/(x2-x1)
    b = y1 - (a*x1)
    outputString += "({0} {1}) ".format(int(a), int(b))

print(outputString.strip())