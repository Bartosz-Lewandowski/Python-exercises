from random import randint 
digit = randint(1,100)
decision = False
n = 0
while decision == False:
    guess = int(input('Zgadnij jaką liczbę wylosował komputer: '))
    n += 1
    if guess < digit:
        print("Twoja liczba jest WIĘKSZA od tej, którą wylosował komputer")
    elif guess > digit:
        print('Twoja liczba jest MNIEJSZA od tej, którą wylosował komputer')
    else:
        print('Brawo! Udało Ci się zgadnąć liczbę! Udało Ci się to zrobić w {} próbach!'.format(n))
        decision = True
