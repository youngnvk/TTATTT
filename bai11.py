
import math
def eratosthenes(n, primes):
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    #cách 1: return sum([i for i in range(2, n + 1) if primes[i]])
    #cách 2:
    sum = 0
    for i in range(2, n + 1):
        if(primes[i]):
            sum += i
    return(sum)
if __name__== '__main__':
    n =int(input("Nhập giá trị của N:"))
    primes = [1] * (n + 1)
    print(eratosthenes(n, primes))
    
    