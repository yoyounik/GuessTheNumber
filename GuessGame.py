import random

def guess(x):
    random_number = random.randint(1, x)
    think = 0
    while think != random_number:
        think = int(input(f"Guess the number between 1 and {x}: "))
        if think < random_number:
            print("Sorry guess again, Too low.")
        elif think > random_number:
            print("Sorry guess again, Too high.")

    print(f"Hurray 🚀 you guessed {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C) ??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Congrats 😊 , the computer guessed your number: {guess}, correctly")




computer_guess(10)

