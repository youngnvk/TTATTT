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
    while(True):
        n = int(input('Nhập n > 0 : '))
        if n > 0:
            break
        else:
            print('Nhập lại!')
    primes = eratosthenes(n) #gán mảng primes = mảng nguyên tố từ eratosthenes
    cnt = 1
    for i in range(len(primes) - 1):
        if (primes[i + 1] - primes[i] == 2): #vì hàm eratosthenes đã sắp xếp từ bé đến lớn
                                            #nên ta chỉ cần tìm số đằng trước trừ đi số đằng sau là đủ.
            print(f'cặp 2 số thỏa mãn thứ {cnt} là : ({primes[i]}, {primes[i + 1]})')
            cnt += 1
    if cnt == 1:
        print('Không tìm thấy!')           
           