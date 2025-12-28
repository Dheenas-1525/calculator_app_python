#using fucntion to build cal app from control cal app:
'''
logic of to build to app using function :

🧠 Concept First (No Code Yet)
Your calculator currently does this inline:
Addition logic
Subtraction logic
Multiplication logic
Division logic
That means:
Repeated structure
Harder to modify later
With functions:
Each operation has one responsibility
Main flow becomes very clear
🧩 What We Will Create (Small Steps)
We will create 4 functions:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
Each function will:
Take inputs
Return a result (or message)
🔹 Function Structure (Understand This)
General form:
def function_name(parameters):
    # logic
    return result
Important:
def defines the function
return sends value back to caller

'''

#use def always to create fucntion in python :
def calcualtor(x, y):
    add = x+y
    sub = x-y
    multi = x*y
    div = x/y
    return add, sub,multi, div

name = input ("Hello user Please enter your good name here :")

print("Welcome {} To My Control Cal App :".format(name))
choice = 'y'
while choice == 'y':

    num1 = float(input("Hey {} Enter your first number ; ".format(name)))
    num2 = float(input("Hey {} Enter your second number here : ".format(name)))
    add, sub, multi, div = calcualtor(num1, num2)
    print("Hey {} Choose which operation you want to execute select anyone of below given")

    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")

    num3 = int(input("enter your operation which one is to be execute "))

    if num3 == 1:
        print("Addition",num1+num2)
    elif num3 == 2:
        print("sub",num1-num2)
    elif num3 == 3:
        print("multiply",num1*num2)
    elif num3 == 4:
        if num2 == 0:
            print('cant divide by zero')
        else:
            print("div",num1/num2)
    else:
        print("Hey {} Please selected valid operation .".format(name))    

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice == 'y':
        print("thanks for choice once again my app ")
    elif choice == 'n':
        print("thanks for using my cal app {} ".format(name))



