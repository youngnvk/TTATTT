#âu 9. Viết chương trình đếm số số nguyên tố nhỏ hơn hoặc bằng N với N được nhập vào từ bàn phím.
import math
def eratosthenes(n, primes):
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
if __name__== '__main__':
    n =int(input("Nhập giá trị của N:"))
    primes = [1] * (n + 1)
    print(len(eratosthenes(n, primes)))
    
    