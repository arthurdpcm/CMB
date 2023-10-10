import numpy as np

def compare_price(correct: int, guess: int):

    tries = 0
    while guess != correct:
        if guess < correct:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        guess = int(input())
        tries += 1
    print("Congratulations, you guessed the price! It took you " + str(tries) + " tries.")

price = np.random.randint(1, 1000)


guess = int(input())

result = compare_price(price, guess)
# 10 steps are sufficient to guess the price
# log2n steps are sufficient to guess the price
