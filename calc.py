while True:
    first = input("First number (or q to quit): ")
    if first == "q":
        print("Bye!")
        break
    op = input("Operation (+ - * /): ")
    second = input("Second number: ")
    try:
        a = float(first)
        b = float(second)
    except ValueError:
        print("Please type real numbers.")
        continue

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("You can't divide by zero.")
            continue
        result = a / b
    else:
        print("I don't know that operation.")
        continue

    if result == int(result):
        result = int(result)
    print("Answer:", result)
