import math
def gcd2(a, b):
    A = a
    B = b
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A
def checkNto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__== '__main__':
    while(True):
        n = int(input('Nhập khoảng N để kiểm tra : '))
        if 2 <= n < 1000:
            break
        else:
            print('Mời bạn nhập lại')
    cnt = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            gcd_a_b = gcd2(i, j)
            if checkNto(gcd_a_b):
                cnt += 1
                print(f'cặp số thứ {cnt} là: {(i, j)}')
                print('')