"""Converts and Returns the number of bits in a given base 10 number"""

def count_bits(n):
    bitlist = []
    count = 0
    while n >= 1:
        j = n%2
        n = int(n//2)
        if j == 0:
            bitlist.append(0)
        else:
            bitlist.append(1)
            count +=1
    #reversing the list to return the correct order of binary 
    bitlist = (bitlist[::-1])
    bitlist = "".join(map(str, bitlist))
    print(bitlist)
    return count



n = 839427196456
print (count_bits(n))
