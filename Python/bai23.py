import math
def eratosthenes_segment(l, r):
    limit = r - l + 1
    primes = [1] * limit
    if l == 0:
        primes[0] = primes[1] = 0 
    if l == 1:
        primes[1] = 0
    for i in range(2, int(math.sqrt(r) + 1)):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
                primes[j - l] = 0      
    return [i for i in range(max(2, l), r + 1) if primes[i - l]] #trả về mảng nguyên tố
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    while True:
        A = int(input('Nhập giá trị của A: '))
        if A > 0:
            break
        else:
            print('Nhập lại !')
    while True:
        B = int(input('Nhập giá trị của B: '))
        if B > A:
            break
        else:
            print('Nhập lại !')
    result1 = sum(eratosthenes_segment(A, B))
    print(f"tổng của các số nguyên tố trong đoạn ({A}, {B}) là :", result1)
    result2 = checknto(result1)
    if result2 == True:
        print('YES')
    else:
        print('NO')