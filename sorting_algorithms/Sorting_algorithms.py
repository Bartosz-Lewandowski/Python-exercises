import random
import time
from tabulate import tabulate
#----------------Create lists to sort---------------#
random.seed(133)
lst = [[random.randint(1,100) for i in range(10)],
       [random.randint(1,100) for i in range(100)],
       [random.randint(1,100) for i in range(1000)],
       [random.randint(1,100) for i in range(10000)]]

#----------------- Time measure -------------#
def timeit(method):
    def timed(lst):
        measurement = {'Elements':[],'Time':[]}
        for i in lst:
            start = time.time()
            method(i)
            end = time.time()
            time_elapsed = end - start
            measurement['Elements'].append(len(i))
            measurement['Time'].append(time_elapsed)
        return (tabulate(measurement,headers=measurement.keys()))
    return timed


#-------------------------------------------#
#-----------------Insert sort---------------#
@timeit
def insert_sort(lst):
    for i in range(1,len(lst)):
        value = lst[i]
        while lst[i-1] > value and i>0:
            lst[i],lst[i-1] = lst[i-1],lst[i]
            i -= 1
    return lst

print('Insert sort:')
print(insert_sort(lst))
print('\n\n')

#--------------Selection sort---------------#
@timeit
def selection_sort(lst):
    for i in range(len(lst)-1):
        lowest_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[lowest_index]:
                lowest_index = j
        if lowest_index != i:
            lst[i],lst[lowest_index] = lst[lowest_index],lst[i]
    return lst
print('Selection sort:')
print(selection_sort(lst))
print('\n\n')
#--------------- Bubble sort ---------------#
@timeit
def bubble_sort(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst


print('Bubble sort:')
print(bubble_sort(lst))
print('\n\n')
#------------------- Quick sort -------------------#

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        lower = []
        greater = []
        equal = []
        pivot = lst[0]
        for i in lst:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                greater.append(i)
            elif i == pivot:
                equal.append(i)
        return quick_sort(lower) + equal + quick_sort(greater)
        

print('Quick sort:')
print(timeit(quick_sort)(lst))
print('\n\n')

