#function unique_in_order which takes as argument
#a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable): 

    iterable = list(iterable)
    if len(iterable) == 0:
        pass
        return []
    new = []
    new.append(iterable[0])
    for i in range(0,len(iterable)-1):
        if iterable[i] == iterable[i+1]:
            pass
        else:
            new.append(iterable[i+1])

    return new

print(unique_in_order('ABBCcAD'))

