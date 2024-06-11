import math
def rivot(N):
    reverse = 0
    while(N != 0):
        r = N  % 10
        N //= 10
        reverse = reverse * 10 + r
    return reverse
def is_prime():
    l = 2
    r = 100000
    primes = [1] * (r - l + 1)
    # Sàng Eratosthenes để tìm các số nguyên tố từ l đến r
    for i in range(2, int(math.sqrt(r)) + 1):
            start = max(i * i, (l + i - 1) // i * i)
            for j in range(start, r + 1, i):
                primes[j - l] = 0   
    # trả về mảng các số nguyên tố từ 100 -> 999
    return [i for i in range(l, r + 1) if primes[i - l]]
if __name__=='__main__':
    array_primes = is_prime()
    for i in range(len(array_primes)):
        daonguoc = rivot(array_primes[i])
        k = round(daonguoc ** (1 / 3))
        if k ** 3 == daonguoc:
            print(array_primes[i])
