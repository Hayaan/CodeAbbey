# http://www.codeabbey.com/index/task_view/arithmetic-progression

n = int(input()); resOut = ""
for i in range(n):
    currList = input().split(); res = int(currList[0]);
    for j in range(1, int(currList[2])):
        res += (int(currList[0]) + j*int(currList[1]))
    resOut += str(res) + " "
print(resOut)