#--------------------1-----------------------------------#
#Find if given word is a polindrom
def polindrom(word):
    word = word.lower()
    word = word.replace(' ','')
    reversed_word = word[::-1]
    if reversed_word == word:
        return('Word {} is a polindrom!'.format(word))
    else:
        return('Word {} is not a polindrom.'.format(word))
print('-------------------Task 1-----------------------')
print(polindrom('bbbaaaabbb'))
print(polindrom('coronavirus'))
print(polindrom('aea'))
print(polindrom('a to kanapa pana kota'))
print('\n\n')

#------------------2------------------#
#Find common letters in two given words
def common_letters(word1,word2):
    common = list(set(word1)&set(word2))
    for i in common:
        yield i
print('-------------------Task 2-----------------------')
words = ['Hello!','Hi! How are you?']
print('Common letters in word "{}" with word "{}":'.format(words[0],words[1]))
for i in common_letters(words[0],words[1]):
    print(i)
    
print('\n')

#--------------------3------------------#
#Fibonacci algorithm
def fibonacci(n):
    result = []
    for i in range(1,n+1):
        if i <= 2:
            result.append(1)
        else:
            new_digit = result[i-2] + result[i-3]
            result.append(new_digit)
    return result
print('-------------------Task 3-----------------------')
print('Fibonacci with list:')
print(fibonacci(10))
print('\n')

#Fibonacci with recurency
def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)
print('Fibonacci with recurency:')
print(fib_rek(10))
print('\n\n')

#--------------------4------------------#
#Estimating pi value
import random 
def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for x in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
            num_point_total += 1
        else:
            num_point_total += 1
    return 4 * num_point_circle/num_point_total
print('-------------------Task 4-----------------------')
print('Pi value with 100 random points:')
print(estimate_pi(100),'\n')

print('Pi value with 1000000 random points:')
print(estimate_pi(1000000))

