import math

def tinhTongUoc(N):
    B = []
    limit = int(math.sqrt(N) + 1)
    for i in range(1, limit):
        if N % i == 0 or i == 1:
            B.append(i)
            if i * i != N:
                B.append(N // i)
    return sum(B) - N

def soThanThien(N):
    for i in range(1, N):
        sum_i = tinhTongUoc(i)
        if sum_i < N:
            sum_j = tinhTongUoc(sum_i)
            if sum_j == i and i != sum_i:
                print(i, sum_i)
if __name__== '__main__':
    N = int(input('Nhập số N vào từ bàn phím : '))
    soThanThien(N)
