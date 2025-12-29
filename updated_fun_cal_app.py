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

    num1 = float(input("enter the first number "))

    num2 = float(input("enter the second number "))


    options = ['1.addtion',
            '2.substraction',
            '3.multiplication',
            '4.division']
    for option in options:
        print(option)
    # print("1.Addition")
    # print("2.Subtraction")
    # print("3.Multiplication")
    # print("4.Division")

    num3 = int(input("choose the options "))
    if num3 == 1:
        print("result of Additon operator is ",add(num1, num2))
    elif num3 == 2:
        print("result of Subtraction operator is ",sub(num1, num2))
    elif num3 == 3:
        print("result of Multiplication operator is ",multi(num1 ,num2))
    elif num3 == 4:
        print("result of Division operator is ",div(num1, num2))
    else:
        print("please choose valid options ....")

    choice = input("Do you want to continue? (y/n): ").lower()
if choice != 'y':
    print("thanks for choose my cal app")