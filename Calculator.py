def calculator():
    ops = {
        "1": lambda a, b: a + b,
        "2": lambda a, b: a - b,
        "3": lambda a, b: a * b,
        "4": lambda a, b: "Error" if b == 0 else a / b,
        "5": lambda a, b: "Error" if b == 0 else a % b,
        "6": lambda a: a ** 2
    }

    print("1:+  2:-  3:*  4:/  5:%  6:square")

    choice = input("Enter choice: ")

    if choice not in ops:
        print("Invalid choice")
        return

    if choice == "6":
        num = float(input("Enter number: "))
        print("Result:", ops[choice](num))
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", ops[choice](a, b))


calculator()