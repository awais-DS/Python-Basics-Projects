while True:
    print("----welcome to Fizz Buzz Game ----")

    try:
        a=int(input("Enter any Number:  "))
        if a%3==0 and a%5==0:
            print("Fizz Buzz")
        elif a%3==0:
            print("Fizz")
        elif a%5==0:
            print("Buzz")
        else:
            print(a)
    except ValueError:
        print("Enter a digits only")
    choice = input("Do you want to run FizzBuzz again? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program... Goodbye!")
        break