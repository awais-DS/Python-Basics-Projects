import random
while True:
    a=random.randint(1,100)
    attempts=0
    print("\nNew game started number is between (1-100) ")

    while True:
        guess=int(input("Enter any number to guess:  "))
        attempts+=1

        if guess>a:
            print("Too Big ! ")
        elif guess<a:
            print("Too small !")
        else:
            print(f"Wow You guessed correctly the number was {a}")
            print(f"You guessed in {attempts} attempts.")
            break
    choice=input("Press space and then enter to continue or any other to exit ")
    if choice==" ":
        print("Programming start again ")
        continue
    else:
        print("Programm ending Good bye ")
        break

