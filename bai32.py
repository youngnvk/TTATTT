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

def modulo(a, k, n):
    if a % m == 0:
        return 0
    b = 1
    A = a
    while(k != 0):
        if k % 2 == 1:
            b = (A * b) % n
        A = (A * A) % n
        k = k // 2
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
