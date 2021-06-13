#This function returns the sum of the two smallest positive integers

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]
