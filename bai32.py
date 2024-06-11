import math
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def tinh_phi(n):
    for i in range(101,500):
        if nto(i):
             for j in range(i, 500):
                 if nto(j) and i * j == n:
                    phi = (i - 1) * (j - 1)
                    print(f"Đã tìm được p = {i} và q = {j} trong khoảng (100, 500)")
                    return phi                
    return None
def gcd(a, b):
    A = a
    B = b
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A
def tinh_e(k):
    if k is None:
        return None
    e = 2
    while(e < k):
        if gcd(e, k) == 1:
            return e
        e += 1
def nghichdao(a, p):
    if a is None or p is None:
        return None
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1 and u != 0:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p

def bin(n):
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr

def modul_power(a, k, n):
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return b
    A = a
    if arr[0] == 1:
        b = a
    for i in range(1, cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b
if __name__=='__main__':
    n = int(input('Nhập số n: '))
    SBD = int(input('Nhập số báo danh: '))
    m = SBD + 123
    k = tinh_phi(n)
    if k is not None:
        e = tinh_e(k) 
        if e is not None:
            d = nghichdao(e, k)
            if d is not None:
                c = modul_power(m, e, n)
                print(f'Thông điệp SBD: {SBD} đã được mã hóa thành bản mã c: {c}')
                #-Giải mã thông điệp, tính m = cd mod n 
                m = modul_power(c, d, n)
                print(f'Bản giải mã thông điệp là m : {m}')
            else:
                print('Không tính được nghịch đảo')
        else:
            print('Không tìm thấy e !') 
    else:
        print('Không tìm thấy cặp số nguyên tố p và q thỏa mãn')       