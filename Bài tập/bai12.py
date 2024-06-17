import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    while(True):
        n = int(input('Nhập giá trị của N: '))
        if n > 0:
            break
        else:
            print('Nhập lại!')      
    primes = eratosthenes(n)
    found = False
    for i in range(len(primes) - 3):
        sum = primes[i] + primes[i + 1] + primes[i + 2] + primes[i + 3]
        if checknto(sum) == 1 and sum <= n:
            print("4 số đó là : ", primes[i], primes[i + 1], primes[i + 2], primes[i + 3])
            found = True
    if found == False:
        print("Không tìm thấy!")
    