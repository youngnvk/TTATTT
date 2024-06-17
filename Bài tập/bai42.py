import random
import math
def bin(k):
    cnt = 0
    arr = []
    while(k != 0):
        r = k % 2
        arr.append(r)
        cnt += 1
        k = k // 2
    return cnt, arr
def modulo(a, k, n): #nhan binh phuong co lap
    cnt, arr = bin(k)
    #chuan bi k
    if k == 0:
        return 1
    b = 1
    A = a 
    if arr[0] == 1:
        b = a 
    for i in range(1, cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (b * A) % n
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
            print(f"a = {a}, thỏa mãn vì {a} ^ {p} % {q} = {k} là số nguyên tố")
    if ok == False:
        print('Không có số a nào thỏa mãn ~')
