import random
import math
import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def random_prime(l, r): #random ra 1 so nguyen to trong khoang 101-499
    while True:
        p = random.randint(l, r)
        if is_prime(p):
            break
    return p

def tinh_phi(p, q): #Tính phi(n) = (p - 1).(q - 1)
    return (p - 1) * (q - 1)

def tinh_d(e, phi):
        return nghichdao(e, phi)
def gcd(a, b):
    A = a
    B = b
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A

def nghichdao(a, p):
    if gcd(a, p) != 1: # điều kiện nghịch đảo
        return False
    u = a
    v = p
    x1 = 1
    x2 = 0
    if u == 0: #không thể chia cho 0
        return False
    while(u != 1):
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u 
        u = r
        x2 = x1
        x1 = x
    return x1 % p

def bin(n):  # Chuyển đổi số nguyên sang dạng nhị phân
    arr = []
    cnt = 0
    while n != 0:
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr

def modulo(a, k, n):  # Hàm tính lũy thừa modulo bằng phương pháp bình phương và nhân
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return b  # 0^0 là 1 theo định nghĩa
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b      
def mahoa(m, e, n):
    return modulo(m, e, n)

def giaima(c, d, n):
    return modulo(c, d, n)
def tim_e(n):
    while(True):
        e = random.randint(1, phi - 1)
        if gcd(e, n) == 1:
            break
    return e
if __name__ == '__main__':
    l = 101
    r = 500
    p = random_prime(l, r)
    while True:
        q = random_prime(l, r)
        if q != p: # p != q thì mới nhận
            break
    print(f"2 số nguyên tố p và q chọn được trong khoảng (100->500) là : {p} và {q}")
    n = p * q
    print(f"giá trị của n = {p} * {q} là : {n}")
    phi = tinh_phi(p, q)
    print(f"giá trị của phi({n}) = {phi}")
    e = tim_e(phi)
    print(f"giá trị e nguyên tố cùng với phi(n) là e = {e}")
    d = tinh_d(e, phi)
    if d == False:
        print(f'Không tìm thấy giá trị d là nghich đảo của e ({e}^-1 mod {n})')
        sys.exit() # kết thúc chương trình
    else:
        print(f"giá trị của d là : {d}")
    SBD = int(input('Nhap So Bao Danh : '))
    m = SBD + 123
    ma_hoa = mahoa(m, e, n)
    print(f'Ma hoa (c) : {ma_hoa}')
    giai_ma = giaima(ma_hoa, d, n)
    print(f'Giai ma (m) : {giai_ma}')
