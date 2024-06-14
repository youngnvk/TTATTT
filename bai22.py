import math

def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return primes

def Fn(n, primes):
    if primes[n] == 1:
        return n
    else:
        return 0

if __name__ == '__main__':
    while True:
        L = int(input('Nhập giá trị của L: '))
        if L > 0:
            break
        else:
            print('Nhập lại !')
    while True:
        R = int(input('Nhập giá trị của R: '))
        if R > L:
            break
        else:
            print('Nhập lại !')
    primes = eratosthenes(10000)  # Để đánh dấu các số nguyên tố < 10000
    result = 0
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            result += Fn(i, primes) * Fn(j, primes)

    print(f'Kết quả là: {result}')
