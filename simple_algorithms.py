def polindrom(word):
    word = word.lower()
    word = word.replace(' ','')
    reversed_word = word[::-1]
    if reversed_word == word:
        return('That word is a polindrom!')
    else:
        return('That word is not a polindrom.')
#print(polindrom('kajak'))
#print(polindrom('Agata'))
#print(polindrom('Ala'))
#print(polindrom('a to kanapa pana kota'))

def common_letters(word1,word2):
    common = list(set(word1)&set(word2))
    for i in common:
        yield i

#for i in common_letters('Hello!','Hi! How are you?'):
#    print(i)

def bubble_sort(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    return a
#print(bubble_sort([3,4,2,90,112,4,3,1,0]))

def star_tringle(n):
    for i in range(1,n + 1):
        if i % 2 != 0:
            ran = n - i
            yield int((ran/2)) * ' ' + i * '*' + int((ran/2)) * ' ' 

for i in star_tringle(7):
  print(i)

def fibonacci(n):
    result = []
    for i in range(1,n+1):
        if i <= 2:
            result.append(1)
        else:
            new_digit = result[i-2] + result[i-3]
            result.append(new_digit)
    return result

# print(fibonacci(3))

def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

#print(fib_rek(10))

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
#print(estimate_pi(100))

