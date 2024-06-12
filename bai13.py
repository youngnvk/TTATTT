import math

def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    while True:
        n = int(input('Nhập giá trị của N: '))
        if n > 0:
            break
        else:
            print('Nhập lại!')

    primes = eratosthenes(n)
    cnt = 1
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            total = primes[i] + primes[j]
            diff = abs(primes[i] - primes[j])
            if is_prime(total) and is_prime(diff) and total <= n:
                print(f"Cặp số thỏa mãn thứ {cnt} : {primes[i]}, {primes[j]}")
                cnt += 1
    if cnt == 1:
        print("Không có cặp số nào thỏa mãn điều kiện.")
