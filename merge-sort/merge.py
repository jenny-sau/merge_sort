# Merge Sort en Python

Ce script implémente l'algorithme de tri fusion (merge sort) en Python.

def merge(array):
    if len(array)<=1:
        return array

    middle_array = len(array)//2
    left_part = array[:middle_array]
    right_part = array[middle_array:]

    merge(left_part)
    merge(right_part)

    index_left_part=0
    index_right_part=0
    index_sorted = 0

    while index_left_part < len(left_part) and index_right_part<len(right_part):
        if left_part[index_left_part] < right_part[index_right_part]:
            array[index_sorted]=left_part[index_left_part]
            index_left_part+=1

        else:
            array[index_sorted]=right_part[index_right_part]
            index_right_part+=1
        index_sorted+=1

    while index_left_part < len(left_part):
        array[index_sorted]=left_part[index_left_part]
        index_left_part += 1
        index_sorted += 1

    while index_right_part < len(right_part):
        array[index_sorted]=right_part[index_right_part]
        index_right_part += 1
        index_sorted += 1

    return array

#Test
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5,100]

    merge(numbers)
    print('Sorted array: '+ str(numbers))
