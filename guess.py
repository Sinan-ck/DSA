import random
number= random.randint(1,100)
attempt=0
print("guess the number btw 1 and 100\n")
while True:
    guess=int(input())
    attempt+=1
    if guess>number:
        print("lower")
    elif guess<number:
        print("higher")
    else:
        print(f"congratulations you guessed the number {number} in {attempt} atampts ")
        break


#Features:

Random number generation using Python's random module
User input handling
Hint system (higher/lower)
Attempt counter
Continuous guessing until the correct number is found

Technologies Used:

Python 3
Random Module
