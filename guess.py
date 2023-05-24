
guess = 0
tries = 0

while guess != 6 and tries != 3:
    guess = int(input("Guess the number(3 trials):  "))
    tries += 1

if guess != 6 and tries == 3:
    print("You've Exhausted your trials")

if guess == 6 and tries != 3:
    print("You got it!")

if guess == 6 and tries == 3:
    print("Wow You got it at your last trial")
