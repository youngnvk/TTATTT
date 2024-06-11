import math

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def bin(n):
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr

def binhphuongcolap(a, k, n):
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return b
    A = a
    if arr[0] == 1:
        b = a
    for i in range(1, cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b

def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return primes

def is_carmichael(n):
    primes = eratosthenes(n) 
    if primes[n] == 1: #so nguyen to khong phai la so chamicel
        return False
    for i in range(2, n):
        if gcd(n, i) == 1:
            if binhphuongcolap(i, n - 1, n) != 1:
                return False
    return True

def main():
    n = int(input("Enter n: "))
    arr = []
    for i in range(2, n + 1):
        if is_carmichael(i):
            cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()
