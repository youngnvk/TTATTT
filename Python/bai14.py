import math
def reversed(N):
    reverse = 0
    while(N != 0):
        r = N  % 10
        reverse = reverse * 10 + r
        N //= 10
    return reverse
def is_prime(l, r):
    limit = (r - l + 1)
    primes = [1] * limit
    # Sàng Eratosthenes để tìm các số nguyên tố từ l đến r
    for i in range(2, int(math.sqrt(r)) + 1):
            start = max(i * i, (l + i - 1) // i * i)
            for j in range(start, r + 1, i):
                primes[j - l] = 0   
    return [i for i in range(l, r + 1) if primes[i - l]]
if __name__=='__main__':
    while(True):
        l = int(input('Nhập giá trị l >= 100: ')) #vì số cần tìm là số 3 chữ số
        if l >= 100:
            break
        else:
            print('Nhập lại l')
    while(True):
        r = int(input('Nhập giá trị l < r < 1000: ')) #vì số cần tìm là số 3 chữ số
        if l < r < 1000:
            break
        else:
            print('Nhập lại r')
    array_primes = is_prime(l, r)
    for i in range(len(array_primes)):
        daonguoc = reversed(array_primes[i])
        k = round(daonguoc ** (1 / 3)) # làm tròn khi mũ với 1 / 3
        if k ** 3 == daonguoc: #kiểm tra
            print("số đó là: ", array_primes[i])
            break
