import numpy as np
import time


#decorator to measure time 
def timeit(method):
    def timed(A,B):
        start = time.time()
        result = method(A,B)
        end = time.time()
        time_elapsed = end - start
        print('Time elapsed:',time_elapsed,'\n')
        return (result)
    return timed

#Generate matrixes with given size 
def generator(size, diag, up, down):
    A = np.zeros((size, size))
    B = np.zeros((size,))
    for i in range(size):
        for k in range(size):
            A[i, i] = diag
            for j in range(i + 1, size):
                A[i, j] = up
            for j in range(i):
                A[i, j] = down
        B[i] = 1.0
    return A, B
#Cramer equation 
@timeit
def Cramer(A, B):
    shape = A.shape[0]
    det = np.linalg.det(A)
    results = np.zeros(shape)
    for column in range(shape):
        column_to_save = np.zeros(shape)
        for row in range(shape):
            column_to_save[row] = A[row][column]
            A[row][column] = B[row]
        detX = np.linalg.det(A)
        result = detX / det
        results[column] = result
        for row in range(shape):
            A[row][column] = column_to_save[row]
    return results

#Check how much result is different from the real results
def Check_correctness(A, B, X):
    shape = A.shape[0]
    checks = np.zeros(shape)
    for i in range(shape):
        suma = 0
        for j in range(shape):
            suma += A[i, j] * x[j]
        checks[i] = suma - B[i]
    return checks
    #returns matrix with numbers that says how wrong results are, the lowest the number the better


A, B = generator(10, 4, 2, 1)


print(Cramer(A,B))
