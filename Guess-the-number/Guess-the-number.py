import random
import time

number = random.randrange(1, 100)
score = 10000
running = True
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def give_hint(num, guess):
    rand = random.randint(1, 5)
    if rand == 1:
        if guess > num:
            return "Your guess is higher than the number"
        else:
            return "Your guess is lower than the number"
    if rand == 2:
        if num in primes:
            return "The number is a prime"
        else:
            return "The number is not a prime"
    if rand == 3:
        if (num % 2) > 0:
            return "The number is not even"
        else:
            return "The number is even"
    if rand == 4:
        if abs(num - guess) < 25:
            return "The number is less than 25 numbers away from your guess"
        else:
            return "The number is more than 25 numbers away from your guess"
    if rand == 5:
        if (num % 5) > 0:
            return "The number is not a mutiple of 5"
        else:
            return "The number is a multiple of 5"


while running == True:
    while True:
        try: 
            guess = int(input("Enter your guess: "))

            break
        except ValueError:
            print("This is not a valid number")
    
    print(f"you guessed {guess}")
    if guess == number:
        print(f"Correct answer! The answer was {number} and you ended up with a score of {round(score)} and you started with a score of 10000")
        running = False
    else: 
        print("This is not the correct answer! Try again")
        print("Here is a hint: " + give_hint(number, guess))
        score *= 0.95

input("")