a = float(input("First number: "))
op = input("Operation (+ - * /): ")
b = float(input("Second number: "))

if op == "+":
    print("Answer:", a + b)
elif op == "-":
    print("Answer:", a - b)
elif op == "*":
    print("Answer:", a * b)
elif op == "/":
    if b == 0:
        print("You can't divide by zero.")
    else:
        print("Answer:", a / b)
else:
    print("I don't know that operation.")
