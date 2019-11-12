import sys
import random

if __name__ == '__main__': 
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    n = random.randint(1, 99)
    guess = 0
    attempts = 0
    while n != guess:
        bye = input("What's your guess between 1 and 99?\n>> ")
        if bye == "exit":
            print("Goodbye!")
            exit()
        try:
            guess = int(bye)
            if guess < n:
                print("Too low!")
            elif guess > n:
                print("Too high!")
        except:
            print("That's not a number.")
        attempts += 1
    if attempts == 1:
        print("Congratulations! You got it on your first try!")
        if n == 42:
             print("The answer to the ultimate question of life, the universe and everything is 42.")
    else:
        print("Congratulations, you've got it!")
        print("You won in {} attempts!".format(attempts))