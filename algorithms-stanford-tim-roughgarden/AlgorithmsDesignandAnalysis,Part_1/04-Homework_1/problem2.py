"""
You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, 
after which its elements are in decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.

unimodal array:
an array that has a sequence of monotonically increasing integers followed by a sequence of monotonically decreasing integers
ex.
[3,5,8,9,10,14,11,4,2,1]
"""

def get_max(array):
    array_lenght = len(array)
    mid = int(array_lenght/2)

    if array_lenght == 2:
        return max(array[0], array[1])
    # if array_lenght == 1:
    #     return array[0]

    if array[mid] > array[mid - 1]: #the max is located right of the mi
        return get_max(array[mid : ]) #get the right and continue
    else:
        return get_max(array[0 : mid]) #get the left and continue


# testing
if __name__ == "__main__":
    print(get_max([2, 3, 4, 21, 43, 52, 51, 18, 11, 9, 6, 1]))