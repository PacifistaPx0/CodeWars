""" Returning an array with zeros sorted to the end of the list """


def move_zeros(array):
    num_array = []
    zero_array = []
    for i in range(len(array)):
        if array[i] == 0:
            zero_array.append(array[i])
        else: 
            num_array.append(array[i])
    array.clear()
    return num_array + zero_array

array = [0, 0, 0, 1, 0, 3, 0, 6, 7]

print(move_zeros(array))
