import sys

def max_sequence(list):
    max_end = 0
    max_far = -sys.maxsize-1
    try:     
        if len(list) == 0:
            return 0

        #check if all elements in list are negative and return 0 if true
        elif all(i<0 for i in list):
            return 0

        else:
            for i in range(len(list)):
                max_end = max_end + list[i]
                if max_end < list[i]:
                    max_end = list[i]
                elif max_far < max_end:
                    max_far = max_end

    except ValueError:
        print("A list is required")
    
    return max_far

print(max_sequence([-1,-2,-5]))
            