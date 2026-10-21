import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while (guess != secret_number):
    if guess < secret_number:
        print("Too low! Try again.⬇️")
    else:
        print("Too high! Try again.⬆️")
    guess = int(input("Guess a number between 1 and 10: "))
print(f"Congratulations!🥳 You guessed the secret number {secret_number}.")
print("End of program.😎")