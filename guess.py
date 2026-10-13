import random
number = random.randint(1, 10)
while True:
    answer = input("Guess a number from 1 to 10: ")
    if not answer.isdigit():
        print("Please type a number.")
        continue
    guess = int(answer)
    if guess == number:
        print("You got it!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
