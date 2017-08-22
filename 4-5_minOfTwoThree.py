#http://www.codeabbey.com/index/task_view/min-of-two
#http://www.codeabbey.com/index/task_view/min-of-three

n = int(input()); outputString = ""
for i in range(n):
    x = min(map(int, input().split()))
    outputString += str(x) + " "
print(outputString.strip())