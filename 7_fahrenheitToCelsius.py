# http://www.codeabbey.com/index/task_view/fahrenheit-celsius

# Supposed to be converting from Fahrenheit to Celsius...
# Fahrenheit (x) to Celsius (y):
# y = (x-32)/1.8

# adapted function from the previous problem (#6)
def rounder(num):
    res = (num%1)*10
    print(res)
    if res >= 5:    
        return int(num) +1
    else:           
        return int(num)

inputList = list(map(int, input().split())); outputString = ""
for i in range(1, len(inputList)):
    outputString += str(rounder((inputList[i]-32)/1.8)) + " "
print(outputString.strip())

# Doesn't round negative Celsius values the way the exercise expects it to.












# The formula for converting from Celsius (x) to Fahrenheit (y) is:
# y = 1.8x + 32

# inputList = list(map(int, input().split())); outputString = ""
# for i in range(1, len(inputList)):
#     outputString += str(rounder(inputList[i]*1.8 + 32)) + " "
# print(outputString.strip())
