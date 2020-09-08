import numpy as np
import time

#decorator to measure time 
def timeit(method):
    def timed(a,b):
        start = time.time()
        result = method(a,b)
        end = time.time()
        time_elapsed = end - start
        print('Time elapsed:',time_elapsed)
        return (result)
    return timed


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

def doPostTr(a, b):
    '''
    input: a - matrix nxn
    b - vector with n length
    it transform this equation to tringle form
    '''
    n = a.shape[0]
    assert a.shape == (n, n)
    assert b.shape == (n,)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            wsp = - a[j, i] / a[i, i]
            for k in range(i, n):
                a[j, k] += wsp * a[i, k]
            b[j] += wsp * b[i]
    return a, b

@timeit
def solve(a, b):
    n = a.shape[0]
    assert a.shape == (n, n)
    assert b.shape == (n,)
    x = np.zeros((n,))
    for i in range(n-1, -1, -1):
        assert a[i,i] != 0.0
        suma = 0.0
        for j in range(i+1, n):
            suma += x[j] * a[i, j]
        x[i] = (b[i] - suma) / a[i, i]
    return x

def sprawdzenie(A, B, X):
    shape = A.shape[0]
    checks = np.zeros(shape)
    for i in range(shape):
        left = 0
        for j in range(shape):
            left += A[i, j] * x[j]
        checks[i] = left - B[i]
    return checks


A, B = generator(5, 4, 2, 1)

print(solve(A,B))

