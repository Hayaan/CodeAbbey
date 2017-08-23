# http://www.codeabbey.com/index/task_view/collatz-sequence

def collatzSeq(aTuple):
    for num in aTuple:
        counter = 0
        while num != 1:
            counter += 1
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
        results.append(str(counter))
    print(' '.join(results))

noNeedForThisValue = input()
results = []
inputTuple = tuple(map(int, input().split()))
collatzSeq(inputTuple)