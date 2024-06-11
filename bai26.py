# Câu 26. Một số được gọi là số mạnh mẽ 
# khi nó đồng thời vừa chia hết cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó.
# Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000).
import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
def work(N):
    primes = eratosthenes(N)
    while(N != 10000):
        for i in primes:
            if N % i == 0 and N % (i * i) == 0:
                return N
        N += 1
    return None
if __name__=='__main__':
    N = 9561  # cho trước
    khaideptrai = work(N)
    if khaideptrai:
        print(f'Đây là số mạnh mẽ hơn số {N} :', khaideptrai)
    else:
        print(f'Không tìm thấy số mạnh mẽ nhỏ hơn số {N}.')
    