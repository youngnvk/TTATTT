#Câu 15. #Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên tố 
#hơn kém nhau 2 đơn vị.
# Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc bằng N, với N được nhập vào từ bàn phím.
import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
if __name__=='__main__':
    n = int(input('Nhập giá trị n: '))
    primes = eratosthenes(n)
    for i in range(len(primes) - 1):
        #7 11 13
            if abs(primes[i + 1] - primes[i] == 2):
                print(f'({primes[i]}, {primes[i + 1]})')
           