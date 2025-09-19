def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("0 is not divisible by any number")
        return None
    return a/b

print(" -: Welcome to my Calculator :-")
print("Operations:- + , - , * , / :-")

while True:
    try:
        num1 = float(input("Enter any number : "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter another number : "))

        if operator == "+":
            print(f"Result: {add(num1, num2)}")
        elif operator == "-":
            print(f"Result: {sub(num1, num2)}")
        elif operator == "*":
            print(f"Result: {mul(num1, num2)}")
        elif operator == "/":
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Invalid operator!")

    except ValueError:
        print("Please enter a valid number!")

    choice = input("\nDo you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator exiting... Goodbye!")
        break
