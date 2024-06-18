import math
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
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
    return primes
if __name__=='__main__':
    A = int(input('Nhập A: '))
    B = int(input('Nhập B: '))
    C = int(input('Nhập C: '))
    while(True):
        m = int(input('Nhập m : '))
        if m > 0:
            break
        else:
            print('Nhập lại')
    while(True):
        l = int(input('Nhập l : '))
        if l > m:
            break
        else:
            print('Nhập lại')
    cnt = 1
    for i in range(m, l + 1):
        sum = A * i * i + B * i + C
        if checknto(sum):
            print(f'số x thoả mãn tổng là nguyên tố thứ {cnt} trong khoảng ({m}, {l})', i)
            cnt += 1
    if cnt == 1:
        print('Không tìm thấy')