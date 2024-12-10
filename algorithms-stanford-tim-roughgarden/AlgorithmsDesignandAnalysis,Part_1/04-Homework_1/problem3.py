"""
You are given a sorted (from smallest to largest) array A 
of n distinct integers which can be positive, negative, 
or zero. You want to decide whether or not there is an 
index i such that A[i] = i. Design the fastest algorithm 
that you can for solving this problem.
"""
import math

def get_element_eql_index(array, lo, hi):
    mid = int((hi - lo) / 2) + lo

    if array[mid] == mid: #then A[i] = i
        return mid
    if lo == hi:
        return None
    if array[mid] > mid: #the cell is bigger
        return get_element_eql_index(array, lo, mid)
    if array[mid] < mid: #cell is smaller
        return get_element_eql_index(array, mid + 1, hi)
    
# testing
if __name__ == "__main__":
    arrays = [
    [-10, -5, 0, 3, 7],
    [-10, -5, -3, -2, -1],
    [1, 2, 3, 4, 5],
    [-1, 0, 2, 4, 6],
    [-20, -10, -1, 1, 3, 5, 7, 9, 10, 15, 25],
    [0],
    [-3, -2, -1, 0, 2, 5, 6, 9],
    [0, 10, 20, 30, 40, 50],
    [-15, -10, -5, -3, 0, 2, 4, 7, 9, 11],
    [-10, -5, -2, 1, 4, 7, 11, 14],
    [0, 1, 2, 3, 4, 5],
    [-100, -50, -20, -10, 5, 10, 15, 20, 25, 30],
    [-1, 0, 1, 3, 11, 14], #3
    [-3, -1, 1, 3, 5, 7], #3
    [2, 3, 4, 5, 6, 7, 8, 9],
    [-10, -5, 2, 8, 12, 17, 20, 25, 30], #2
    [100, 101, 102, 103, 104, 105, 106],
    [-10, -5, -2, 1, 4, 7, 8], #4
    [-1],
    [-100, -50, -25, 0, 25, 50, 75, 100]
    ]
    for i, array in enumerate(arrays):
        result = get_element_eql_index(array, 0, len(array) - 1)
        print(i, ") index: ", result if result is not None else "No number found")