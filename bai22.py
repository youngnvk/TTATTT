import random

def bin(n):  # Convert to binary
    arr = []
    while n != 0:
        arr.append(n % 2)
        n = n // 2
    return arr

def nhanbinhphuongcolap(a, k, n):  # Modular exponentiation
    arr = bin(k)
    b = 1
    A = a
    if arr[0] == 1:
        b = a
    for i in range(1, len(arr)):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b

def is_prime(n, t):  # Primality test
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for _ in range(t):
        a = random.randint(2, n - 2)
        if nhanbinhphuongcolap(a, n - 1, n) != 1:
            return False
    return True

def F(n, t):
    return n if is_prime(n, t) else 0

if __name__ == '__main__':
    L = int(input('Nhập giá trị của L: '))
    R = int(input('Nhập giá trị của R > L: '))
    t = int(input('Nhập giá trị của t: '))

    primes = [F(i, t) for i in range(L, R + 1)]

    result = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            result += primes[i] * primes[j]

    print(f'Kết quả: {result}')
