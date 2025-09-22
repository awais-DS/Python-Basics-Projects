while True:
    print("\n---- Welcome to File Reader & Writer ----")
    print("1. Write to file")
    print("2. Read from file")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        text = input("Enter text to write into the file: ")
        with open("mydata.txt", "a") as file:  # 'a' means append mode
            file.write(text + "\n")
        print("✅ Text written to mydata.txt successfully!")

    elif choice == "2":
        try:
            with open("mydata.txt", "r") as file:
                content = file.read()
                if content:
                    print("\n---- File Content ----")
                    print(content)
                else:
                    print("⚠️ The file is empty.")
        except FileNotFoundError:
            print("⚠️ File does not exist yet! Please write something first.")

    elif choice == "3":
        print("👋 Exiting program... Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
