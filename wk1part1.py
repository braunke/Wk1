from random import randint

print('Choose a number between 1 and 9')
#rang of numbers looking through
randomNumber = randint(1,9)
guess = 0
#compares guess to random number
while guess != randomNumber:
    guess = input()
    guess = int(guess)
    if guess > randomNumber:
        print('Too big')
    elif guess < randomNumber:
        print('Too small')
    else:
        print('correct')
        break