import random
number = random.randint(1, 100)
tries = 0
while True:
    answer = input("Guess a number from 1 to 100: ")
    if not answer.isdigit():
        print("Please type a number.")
        continue
    guess = int(answer)
    tries += 1
    if guess == number:
        print("You got it in", tries, "tries!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
