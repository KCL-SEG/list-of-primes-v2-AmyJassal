"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError
    list = []
    a = 2
    list.append(a)
    while(len(list) < number_of_primes):
        a+=1
        isPrime = True
        for num in range(2,a):
            if(a % num == 0):
                isPrime = False
        if(isPrime):
            list.append(a)
    return list
