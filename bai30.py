import math

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def bin(n):  # Chuyển đổi số nguyên sang dạng nhị phân
    arr2 = []
    cnt = 0
    while n != 0:
        r = n % 2
        arr2.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr2

def modulo(a, k, n):  # Hàm tính lũy thừa modulo bằng phương pháp bình phương và nhân
    cnt, arr2 = bin(k)
    b = 1
    if k == 0:
        return 1  # 0^0 là 1 theo định nghĩa
    A = a
    if arr2[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai
        A = (A * A) % n
        if arr2[i] == 1:
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
            if modulo(i, n - 1, n) != 1:
                return False
    return True

if __name__ == "__main__":
    while(True):
        n = int(input('Nhap N: '))
        if 0 <= n <= 10000:
            break
        else:
            print('Nhập lại')
    arr = []
    for i in range(2, n + 1):
        if is_carmichael(i):
            arr.append(i)
    print(f"tổng của các số carmichael là : {sum(arr)}")