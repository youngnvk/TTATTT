import math
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def bin(n):  # Chuyển đổi số nguyên sang dạng nhị phân
    arr2 = []
    cnt = 0
    while n != 0:
        r = n % 2
        arr2.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr2

def modulo(a, k, n):  # Hàm tính lũy thừa modulo bằng phương pháp bình phương và nhân
    cnt, arr2 = bin(k)
    b = 1
    if k == 0:
        return 1  # 0^0 là 1 theo định nghĩa
    A = a
    if arr2[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai
        A = (A * A) % n
        if arr2[i] == 1:
            b = (A * b) % n
    return b
if __name__ == '__main__':
    while( 0 < a < 1000):
        a = int(input('Nhap a: '))
        if 0 < a < 1000:
            break
    while( 0 < k < 1000):
        k = int(input('Nhap k: '))
        if 0 < k < 1000:
            break
    while( 0 < n < 1000):
        n = int(input('Nhap n: '))
        if 0 < n < 1000:
            break 
    test = modulo(a, k, n)
    if test:
        print('Nguyen to')
    else:
        print('Hop so')
