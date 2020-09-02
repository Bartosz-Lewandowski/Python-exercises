import time
from tabulate import tabulate
#----------------Create lists to sort---------------#
lst = [[i for i in range(1000)],
       [i for i in range(10000)],
       [i for i in range(100000)],
       [i for i in range(1000000)]]

figures = [i[-1] for i in lst]
#----------------- Time measure -------------#
def timeit(method):
    def timed(lst,figure):
        measurement = {'Elements':[],'Time':[]}
        for i in range(len(lst)):
            start = time.time()
            method(lst[i],figures[i])
            end = time.time()
            time_elapsed = end - start
            measurement['Elements'].append(len(lst[i]))
            measurement['Time'].append(time_elapsed)
        return (tabulate(measurement,headers=measurement.keys()))
    return timed
#---------------Linear Search--------------#
@timeit
def searching(lst,figure):
    for i in lst:
        if i == figure:
            return i

print('Normal search:')
print(searching(lst,figures))
print('\n\n')
#---------------Biscetion Search----------------#
@timeit
def bisection(lst,figure):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high) // 2
        guess = lst[mid]
        if guess == figure:
            return mid
        if guess > figure:
            high = mid -1
        else:
            low = mid +1

print('Bisection search:')
print(bisection(lst,figures))
print('\n\n')