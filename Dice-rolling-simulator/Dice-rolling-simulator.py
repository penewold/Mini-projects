import random
import time

while True:
    for i in range(3):
        print(".")
        time.sleep(0.5)
    
    print("The number chosen was:")
    print(random.randrange(1, 6))

    command = input("Do you want to make a new number? (y/n): ")
    while True:
        if command == "y":
            break
        elif command == "n":
            break
            
        else:
            print("That isnt valid")
        command = input("Do you want to make a new number? (y/n): ")
    if command == "n":
        break

    