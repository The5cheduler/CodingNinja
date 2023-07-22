import sys
import sys

def maxSubarraySum(arr, n) :
    current_max = arr[0]
    max_of_subarray = arr[0]
    for i in range(1, n):
        current_max = max(arr[i], current_max + arr[i])
        max_of_subarray = max(current_max,max_of_subarray)
    # return the answer
    return max_of_subarray if max_of_subarray > 0 else 0