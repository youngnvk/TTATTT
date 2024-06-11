import random
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        p = random.randint(101, 499)
        if is_prime(p):
            return p

def compute_phi(p, q):
    return (p - 1) * (q - 1)

def compute_d(e, phi):
    return modulo(e, -1, n)

def bin(n):
    cnt = 0
    arr = []
    while(n != 0):
        r = n % 2
        arr.append(r)
        n = n // 2
        cnt += 1
    return cnt, arr
def modulo(a, k, n):
    cnt, arr = bin(n)
    b = 1
    if k == 0:
        return 0
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(cnt):
        A = (a * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b
def encrypt(m, e, n):
    return modulo(m, e, n)

def decrypt(c, d, n):
    return modulo(c, d, n)

if __name__ == '__main__':
    p, q = generate_prime(), generate_prime()
    n = p * q
    phi = compute_phi(p, q)
    e = random.randint(2, phi - 1)
    d = compute_d(e, phi)

    SBD = int(input('Nhap ma sinh vien : '))
    m = SBD + 123

    c = encrypt(m, e, n)
    print(f'Encrypted : (c): {c}')

    decrypted_m = decrypt(c, d, n)
    print(f'Decrypted : (m): {decrypted_m}')
