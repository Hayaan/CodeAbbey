# http://www.codeabbey.com/index/task_view/dice-rolling

n = int(input()); result = ""
for i in range(n):
    # m = float(input()) * n
    # m /= (n/6)                Should've just been the subsequent line. x*n / (n/6) is the same as x*6
    m = float(input()) * 6
    result += str(int(m) + 1) + " "
print(result.strip())
