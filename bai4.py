import math

def segment_primes(l, r):
    limit = r - l + 1
    # Giả sử tất cả các số là nguyên tố ban đầu 
    primes = [1] * limit
    if l < 2:
        primes = [0, 0]  # 0 và 1 không phải số nguyên tố:
    for i in range(2, int(math.sqrt(r)) + 1):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
            primes[j - l] = 0  # Bỏ đánh dấu các bội số của i

    return [i for i in range(max(2,l), r + 1) if primes[i - l]]

if __name__ == '__main__':
    A = int(input('Nhập giá trị của A: '))
    B = int(input('Nhập giá trị của B: '))
    print(segment_primes(A, B))
