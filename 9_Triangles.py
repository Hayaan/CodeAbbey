# http://www.codeabbey.com/index/task_view/triangles

def triangleCheck(aTuple):
    a, b, c = aTuple[0], aTuple[1], aTuple[2]
    if a+ b <= c or a + c <= b or b + c <= a:
        return "0 "
    else:
        return "1 "

n = int(input()); outputString = ""
for i in range(n):
    currTup = tuple(map(int, input().split()))
    outputString += triangleCheck(currTup)
print(outputString.strip())