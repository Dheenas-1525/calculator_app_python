#using control to build calaculator app from simple logic app:


"""
So this is the logic to build using control structure app:
start
↓
ask name
↓
ask number1
↓
ask number2
↓
ask operator
↓
if operator is "+"
    add
elif operator is "-"
    subtract
elif operator is "*"
    multiply
elif operator is "/"
    if number2 == 0
        print error
    else
        divide
else
    invalid operator
↓
end

finaly add while conditions 

"""

#code is here:

name = input ("Hello user Please enter your good name here :")

print("Welcome {} To My Control Cal App :".format(name))
choice = 'y'
while choice == 'y':

    num1 = float(input("Hey {} Enter your first number ; ".format(name)))
    num2 = float(input("Hey {} Enter your second number here : ".format(name)))

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
