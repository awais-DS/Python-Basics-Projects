while True:
    print("----Welcome to Even/Odd Checker----")
    try:
        a = int(input("Enter any Number: "))
        
        def check(num):
            if num % 2 == 0:
                return "Even"
            else:
                return "Odd"
        
        print(f"The number {a} is {check(a)}")
    
    except ValueError:
        print("Enter a valid number please!")
    
    choice = input("Do you want to check another number? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program... Goodbye!")
        break
