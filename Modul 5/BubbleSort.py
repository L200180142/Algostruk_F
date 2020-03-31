L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

def swap(A, p , q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j+1]:
                swap(A, j,j+1)

bubbleSort(L)
