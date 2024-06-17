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
    cnt = 1
    Dakiemtra = []
    for i in range(1, N):    
        if i not in Dakiemtra:
            sum_i = tinhTongUoc(i) 
            if sum_i < N:
                sum_j = tinhTongUoc(sum_i)
            if sum_j == i and i != sum_i:
                Dakiemtra.append(sum_i)
                print(f'cặp số thân thiện thứ {cnt} là :', end="")
                cnt += 1
                print(f'({i}, {sum_i})')
    if cnt == 1:
        print('Không tìm thấy cặp số nào !')
if __name__== '__main__':
    while(True):
        N = int(input('Nhập số N vào từ bàn phím : '))
        if N > 0:
            break
        else:
            print('Nhập lại n!')
    soThanThien(N)       
