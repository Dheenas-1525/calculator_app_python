#!/usr/bin/env python3

def main():
    # ===== Colors =====
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # ===== Logo =====
    logo = """
    ██████╗ ██╗  ██╗███████╗███████╗███╗   ██╗ █████╗ 
    ██╔══██╗██║  ██║██╔════╝██╔════╝████╗  ██║██╔══██╗
    ██║  ██║███████║█████╗  █████╗  ██╔██╗ ██║███████║
    ██║  ██║██╔══██║██╔══╝  ██╔══╝  ██║╚██╗██║██╔══██║
    ██████╔╝██║  ██║███████╗███████╗██║ ╚████║██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
    """


    print(GREEN + BOLD + logo + RESET)
    print(RED + "Welcome to My Calculator  CLI Application" + RESET)
    print(CYAN + "With great power comes great responsibility. Happy learning." + RESET)
    print("-" * 60)



    def add(x, y):
    # print("Result of additon is :",x+y)
        return x+y

    def sub(x, y):
        #print("result of Substraction is :", x-y)
        return x-y

    def multi(x, y):
        return x*y

    def div(x, y):
        if y == 0:
            return "error : can't divide by zero"
        return x/y


    name = input("Enter  your name :  ")
    print("Welcome {} To My CLI Calculator APP".format(name))

    operations = {
            1 : add,
            2 : sub,
            3 : multi,
            4 : div
        }

    messages = {
            1 : "Result of Addition is : " ,
            2 : "Result of Subtraction is : ",
            3 : "Result of Multiplication is : ",
            4 : "Result of Division is : "

        }

    choice = 'y'
    while choice == 'y':
        

    

        try:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            num3 = int(input("choose the options :  "))
            
        except ValueError as numeric_number:
            print("enter only numeric values here ...")
            continue

        if num3 in operations:
            result = operations[num3](num1, num2)
            # if num3== 1:
            #     print("Result of additon is ",num3)
            # elif num3 == 2:
            #     print("Result of substraction is :",num3)
            print(messages[num3],result)
        else:
            print("choose correct first ...")

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("thanks for choosing this app regards dheena")

if __name__ == "__main__":
    main()