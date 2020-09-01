from random import randint 
digit = randint(1,100)
decision = False
n = 0
while decision == False:
    guess = int(input('Guess which number computer chose: '))
    n += 1
    if guess < digit:
        print("Your number is LOWER than computer's choosen number")
    elif guess > digit:
        print("Your number is GREATER than computer's chosen number")
    else:
        print('Congrats! You guessed the number correctly! You did it in {} tries!'.format(n))
        decision = True
