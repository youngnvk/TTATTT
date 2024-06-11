import random

def modulo(a, k, n): #nhan binh phuong co lap
    if a % m == 0:
        return 0
    b = 1
    A = a
    while k != 0:
        if k % 2 != 0:
            b = (b * A) % n
        A = (A * A) % n
        k = k // 2
    return b

def phantich(n):
    x = n - 1
    s = 0
    while x % 2 == 0:
        s += 1
        x = x // 2
    r = x
    return s, r

def miller(n, t):
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

if __name__ == '__main__':
    t = int(input('Nhập số lần lặp: '))
    while True:
        n = int(input('Nhập N: '))
        if 0 < n < 1000:
            break
        else:
            print('Mời bạn nhập lại!')

    p = int(input('Nhập p: '))
    ok = False
    for a in range(n):  # Thêm 1 để kiểm tra cả giá trị a = 0
        k = modulo(a, p, n)
        if miller(k, t) == True:
            print(f"a = {a}, thỏa mãn {a} ^ {p} % {n} là số nguyên tố")
            print('')
            ok = True
    if ok == False:
        print('Không có số nào thỏa mãn!')
