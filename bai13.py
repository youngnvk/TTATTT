#Câu 13. Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N với N 
# nhập vào từ bàn phím,
# sao cho tổng và hiệu của chúng đều là số nguyên tố.
import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
def checkNto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    n = int(input('Nhập giá trị của N: '))
    primes = eratosthenes(n)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if checkNto(primes[i] + primes[j]) and checkNto(abs(primes[i] - primes[j])):
                print(primes[i], primes[j])
                ##Bài lỏ