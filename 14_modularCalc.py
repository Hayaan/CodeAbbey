# http://www.codeabbey.com/index/task_view/modular-calculator

initVal = int(input()); lastStep = False
while not lastStep:
    operator, val = map(str, input().split())
    if operator == '+':
        initVal += int(val)
    elif operator == '*':
        initVal *= int(val)
    else:
        initVal %= int(val)
        lastStep = True

print(initVal)