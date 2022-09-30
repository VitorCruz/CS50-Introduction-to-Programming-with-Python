
import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                print("Integer must be positive")
            else:
                break
        except ValueError:
            print("Input an integer")

    rand_number = random.randint(0,n)

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {n}: "))
            if guess <= 0:
                print("Number must be positive.")
            elif guess > n:
                print(f"I said between 1 and {n}...")
            elif guess == rand_number:
                sys.exit(f"Just right! The correct number was {rand_number}.")
            elif guess > rand_number:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            print("Input an integer, please.")
            
        except EOFError:
            print("Givin' up eh?")

if __name__ == "__main__":
    main()