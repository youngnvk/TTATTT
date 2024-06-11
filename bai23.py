import math
def eratosthenes_segment(l, r):
    limit = r - l + 1
    primes = [1] * limit
    if l < 2:
        primes[0] = primes[1] = 0 #gán 2 thằng ban đầu là 0
    for i in range(2, int(math.sqrt(r) + 1)):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
                primes[j - l] = 0      
    return [i for i in range(max(2, l), r + 1) if primes[i - l]]
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    l = int(input('nhập giá trị của A: '))
    r = int(input('nhập giá trị của B: '))
    result1 = sum(eratosthenes_segment(l, r))
    result2 = checknto(result1)
    if result2 == True:
        print('Yes')
    else:
        print('No')