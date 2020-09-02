import random
import time
from tabulate import tabulate
#----------------Create lists to sort---------------#
random.seed(133)
lst = [[random.randint(1,100) for i in range(10)],
       [random.randint(1,100) for i in range(100)],
       [random.randint(1,100) for i in range(1000)],
       [random.randint(1,100) for i in range(10000)]]
#--------------- Bubble sort ---------------#
def bubble_sort(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

print('Bubble sort:')
measurment = {'Elements':[],'Time':[]}
for i in lst:
    start = time.time()
    bubble_sort(i)
    end = time.time()
    time_elapsed = end - start
    measurment['Elements'].append(len(i))
    measurment['Time'].append(time_elapsed)
print(tabulate(measurment,headers=measurment.keys()))
print('\n')

#------------------- Quick sort -------------------#
