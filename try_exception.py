def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def multi(x, y):
    return x*y

def div(x, y):
    if y == 0:
        return "error : cannot divide by zero"
    else:
        return x/y

    


choice = 'y'

while choice == 'y':

    try:
        num1 = float(input("enter the first number "))
        num2 = float(input("enter the second number "))
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        num3 = int(input("choose the options "))
        
    except ValueError:
        print("enter valid numbers only")
        continue   # 🔥 THIS IS THE KEY LINE

    if num3 == 1:
        print(add(num1, num2))
    elif num3 == 2:
        print(sub(num1, num2))
    elif num3 == 3:
        print(multi(num1, num2))
    elif num3 == 4:
        print(div(num1, num2))
    else:
        print("please choose option 1–4")

    choice = input("Do you want to continue? (y/n): ").lower()

print("thanks for choosing my cal app")
