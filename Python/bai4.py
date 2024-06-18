import math

def segment_primes(l, r):
    limit = r - l + 1
    # Giả sử tất cả các số là nguyên tố ban đầu 
    primes = [1] * limit
    if l == 0: # mảng bắt đầu từ 0 nên [0] = [1] = 1
        primes[0] = primes[1] = 0
    if l == 1: # mảng bắt đầu từ 1 nên chỉ có [1] = 0
        primes[1] == 0
    for i in range(2, int(math.sqrt(r)) + 1):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
            primes[j - l] = 0  # Bỏ đánh dấu các bội số của i

    return [i for i in range(max(2,l), r + 1) if primes[i - l]] #trả về mảng khi primes[i - l] == 1

if __name__ == '__main__':
    while(True):
        print('Vui lòng nhập A và B sao cho (B > A).')
        A = int(input('Nhập giá trị của A: '))
        B = int(input('Nhập giá trị của B: '))
        if B > A:
            break
        else:
            print('Mời bạn nhập lại!')
    print(f'Các số nguyên tố nằm trong khoảng [{A}, {B}] là : ')
    print(segment_primes(A, B))