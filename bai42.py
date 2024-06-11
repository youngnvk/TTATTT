import random
import math

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

def phantich(n):  # Hàm phân tích số n-1 thành dạng 2^s * r
    x = n - 1
    s = 0
    while x % 2 == 0:
        s += 1
        x = x // 2
    r = x
    return s, r

def miller(n, t):  # Hàm kiểm tra nguyên tố Miller-Rabin
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, r = phantich(n)
    for i in range(t):
        a = random.randint(2, n - 2)
        y = modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = modulo(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

def random_primes(n, t):  # Hàm sinh số nguyên tố ngẫu nhiên nhỏ hơn n
    while True:
        a = random.randint(2, n)
        if miller(a, t):
            return a
    
if __name__ == '__main__':
    t = int(input('Nhập số lần lặp: '))
    ok = False
    p = random_primes(1000, t)
    while True:
        q = random_primes(1000, t)
        if q != p:
            break
    print(f'p và q là 2 số nguyên tố ngẫu nhiên được tạo ra: p = {p}, q = {q}')
    for a in range(1, 100):  # Bắt đầu từ 1 để tránh trường hợp a=0
        k = modulo(a, p, q)
        if miller(k, t):
            ok = True
            print(f"a = {a}, thỏa mãn {a} ^ {p} % {q} = {k} là số nguyên tố")
    if not ok:
        print('Không có số a nào thỏa mãn ~')
