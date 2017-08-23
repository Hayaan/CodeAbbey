# http://www.codeabbey.com/index/task_view/bubble-in-array

def bubble(aString):
    aList = list(map(int, aString.split())); res = 0
    counter = 0
    for i in range(len(aList)-2):
        if aList[i+1] < aList[i]:
            aList[i+1], aList[i] = aList[i], aList[i+1]
            counter += 1

#17 Checksum of an array
    for j in range(len(aList)-1):
        res += aList[j]
        res *= 113
        res %= 10000007
    return str(counter) + " " + str(res)

aString = input()
print(bubble(aString))


