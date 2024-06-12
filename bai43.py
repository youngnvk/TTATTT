import random

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
    b = 1
    if k == 0:
        return 1
    A = a 
    if arr[0] == 1:
        b = a 
    for i in range(1, cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (b * A) % n
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
def random_search(n, t): #random 1 so nguyen to
    while(True):
        k = random.randint(2, n)
        if miller(k, t):
            return k
if __name__ == '__main__':
    t = int(input('Nhập số lần lặp: '))
    while True:
        n = int(input('Nhập N: '))
        if 0 < n < 1000:
            break
        else:
            print('Mời bạn nhập lại!')

    p = random_search(n, t)
    print('Số p lựa chọn là: ', p)
    ok = False
    for a in range(n): 
        k = modulo(a, p, n)
        if miller(k, t) == True:
            print(f"a = {a}, thỏa mãn ({a} ^ {p}) % {n} = {k} là số nguyên tố")
            print('')
            ok = True
    if ok == False:
        print('Không có số nào thỏa mãn!')
