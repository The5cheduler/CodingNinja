from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:

    # Write your code here.
    index = -1
    n = len(A)
    for i in range(n-2, -1, -1):
        if A[i] < A[i+1]:
            index = i
            break
    if index == -1:
        A.reverse()
        return A
    
    
    for i in range(n-1, index, -1):
        if A[i] > A[index]:
            A[i], A[index] = A[index], A[i]
            break
    
    A[index+1:] = reversed(A[index+1:])
    return A