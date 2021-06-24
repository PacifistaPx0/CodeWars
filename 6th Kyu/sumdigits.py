#Reduces the sum of the individual digits to a single digit 

def digital_root(n):
    n = list(str(n))
    while len(n)>1:
        j =0
        for i in range(0, len(n)):
            j +=int(n[i])
        n = list(str(j))
    k = "".join(n)
    return int(k)

n = 12345

print(digital_root(n))
