"""This program takes in an int and returns the ipv4 adress"""

def int32_to_ip(n):
    binary_n = f'{n:032b}' #convert decimal to binary in 32 bit format
    ipv4 = ''
    k = 0
    while True:
        if k==32:
            break
        else:
            ipv4 += str(int(binary_n[k:k+8], 2)) + "." #int(binary number, 2) to convert to decimal
        k+=8

    return (ipv4[:-1])


print(int32_to_ip(2234060005))