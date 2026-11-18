num = 7

guess = int(input("Guess the number :"))
while guess != num:
    print("Try again!")
    guess = int(input("Guess the number :"))
print("Correct ! You guessed it.")