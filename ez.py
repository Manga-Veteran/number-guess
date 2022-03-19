import random

num = random.randint(0, 100)


guess = 101
while guess != num:


    guess = int(input('guess a number between 0 and 100: '))


    if guess < num:
        print('your guess is less than the number')
    
    elif guess == num:
        print('too gud')
    
    elif guess > num:
        print('too much')

    