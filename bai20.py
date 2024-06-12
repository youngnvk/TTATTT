import math
def gcd(a, b): #Hàm tính ước chung lớn nhất
    A = a
    B = b
    while B > 0:
        R = A % B
        A = B
        B = R
    return A
if __name__ == '__main__':
    while(True):
        M = int(input('Nhập M (0 < M < 1000): '))
        if 0 < M < 1000:
            break
        else:
            print('Nhập lại M')
    while(True):
        N = int(input('Nhập N (0 < N < 1000): '))
        if 0 < N < 1000:
            break
        else:
            print('Nhập lại N')
    while(True):
        D = int(input('Nhập D (0 < D < 1000): '))
        if 0 < D < 1000:
            break
        else:
            print('Nhập lại D')
    cnt = 1
    for i in range(M, N + 1):
        for j in range(i, N + 1):
            if gcd(i, j) == D:
                print(f'cặp số thứ {cnt} thỏa mãn là: ({i}, {j})')
                cnt += 1
    if cnt == 1:
        print('Không có cặp nào thỏa mãn!')
#M = 2
# N = 50
# D = 11    
    