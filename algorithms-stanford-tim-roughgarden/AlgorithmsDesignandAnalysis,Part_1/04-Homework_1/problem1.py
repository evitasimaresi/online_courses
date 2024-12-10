"""
You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
Give an algorithm that identifies the second-largest number in the array, and that uses at most (n + log_2n - 2) comparisons.
"""

def get_second_largest_number(array_1):
    def get_largest_number(array):
        array_lenght = len(array)
        
        # base case
        if array_lenght == 1:
            return array

        sub_array_1 = get_largest_number(array[0:int(array_lenght/2)])
        sub_array_2 = get_largest_number(array[int(array_lenght/2): ])

        if sub_array_1[0] > sub_array_2[0]:
            sub_array_1.append(sub_array_2[0])
            return sub_array_1
        else:
            sub_array_2.append(sub_array_1[0])
            return sub_array_2
        
    largest_array = get_largest_number(array_1)[1:]
    second_largest_number = largest_array[0]
    for item in largest_array:
        if item > second_largest_number:
            second_largest_number = item
    return second_largest_number

# testing
print(get_second_largest_number([3,1,10,17,12,4]))