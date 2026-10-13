import random
number = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))
if guess == number:
    print("You got it!")
else:
    print("Nope, it was", number)
