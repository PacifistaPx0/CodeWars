"""The aim of the kata is to decompose n! (factorial n) into its prime factors.

Examples:

n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once."""

def decomp(n):
    #code for prime numbers
    primes = []
    for number in range(1, n+1):
        count = 0
        j= number//2+1
        for i in range(2, j):
            if number%i == 0:
                count+=1
                break
        if count ==0 and number != 1:
            primes.append(number)
    output = ""
    for i in primes:
        power = 0
        k = 1
        if i > 2 and i<=n//2:
            while i ** k <= n:
                power += n//(i**k)
                k+=1
            output += f" * {i}^{power}"
        if i > 2 and i>n//2:
            output += f" * {i}"
        if i ==2:
            while i ** k < n:
                power += n//(i**k)
                k+=1
            output += f"{i}^{power}"

    return output


print(decomp(25))
