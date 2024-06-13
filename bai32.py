import random
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def random_prime():
    while True:
        p = random.randint(101, 499)
        if is_prime(p):
            return p

def tinh_phi(p, q):
    return (p - 1) * (q - 1)

def tinh_d(e, phi):
    return modulo(e, -1, n)

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
def encrypt(m, e, n):
    return modulo(m, e, n)

def decrypt(c, d, n):
    return modulo(c, d, n)

if __name__ == '__main__':
    p, q = random_prime(), random_prime()
    n = p * q
    phi = tinh_phi(p, q)
    e = random.randint(2, phi - 1)
    d = tinh_d(e, phi)

    SBD = int(input('Nhap ma sinh vien : '))
    m = SBD + 123

    c = encrypt(m, e, n)
    print(f'Ma hoa : (c): {c}')

    decrypted_m = decrypt(c, d, n)
    print(f'Giai ma : (m): {decrypted_m}')
