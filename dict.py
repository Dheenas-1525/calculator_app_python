def add(x, y):
    print("result of addition is : ", x+y)
    return add

def sub(x, y):
    print("Result of substraction is :", x-y)
    return sub

def multi(x, y):
    print("Result of multi is :",x*y)
    return multi

def div(x, y):
    print("result of div is :",x/y)
    return div



operation ={
    1:add,
    2:sub,
    3:multi,
    4:div
}

try:
    num1 = float(input("enter the first number"))
    num2 = float(input("enter the second number"))
except ValueError:
    print("enter correct format ...")
    
    num3 = int(input("choose the options you want do operations : "))


if num3 in operation:
    result = operation[num3](num1, num2)
else:
    print("choose the correct option..")

print("thanks for choosing my cal app")


