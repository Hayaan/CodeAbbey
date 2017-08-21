# http://www.codeabbey.com/index/task_view/average-of-array

n = int(input()); resultList = []; resString = ""
for i in range(n):
    currSum = 0
    currList = list(input().split())
    for num in currList:
        currSum += int(num)
    resultList.append(currSum/(len(currList)-1))
for resNum in resultList:
    resString += str(round(resNum)) + " "
print(resString)