while True:
    print("----Welcome to average Calculator----")

    numbers=[]

    while True:
        try:
            num=float(input("Enter a number : "))
            numbers.append(num)
        except ValueError:
            print("Please Enter only Numbers")
            continue

        choice=input("Enter space for adding more numbers or any other key if no : ")
        if choice!=" ":
            break
    average=sum(numbers)/len(numbers)
    print(f"Average: {average}")

    again=input("Enter space for starting again or another key for no : ")
    if again!=" ":
        print("----Thank you For Using----")
        break

