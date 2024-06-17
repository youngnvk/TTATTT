import random
def phantich(n): #ham chuan bi s va r
    x = n - 1
    s = 0
    while x % 2 == 0:
        s += 1
        x = x // 2
    r = x
    return s, r
def bin(n): #ham chuyen sang nhi phan
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n / 2
    return cnt, arr
def modulo(a, k, n): #hàm nhân bình phương có lặp
    cnt, arr = bin(n)
    b = 1
    if a % n == 0:
        return 0
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b
def miller(n, t):
    #Kiem tra nhanh
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, r = phantich(n)
    for i in range(t): #duyet so lan t
        a = random.randint(2, n - 2) #random
        y = modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1 #gan j = 1
            while j <= s - 1 and y != n - 1:
                y = (y * y) % 2
                if y == 1:
                    return False
                j = j + 1
            if y != n - 1:
                return False
    return True
if __name__=='__main__':
    n = int(input('Nhập giá trị của n: '))
    t = int(input('Nhap vao gia tri t: '))
    k = miller(n, t)
    if k:
        print('Nguyen to')
    else:
        print('Hop so')
