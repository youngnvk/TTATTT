import math
def reversed(N): #hàm đảo ngược 1 số
    reverse = 0
    while(N != 0):
        r = N  % 10
        reverse = reverse * 10 + r
        N //= 10
    return reverse
def checkNto(N): #hàm check nguyên tố
    if N < 2:
        return False
    for i in range(2, int(math.sqrt(N)) + 1, 1):
        if N % i == 0:
            return False
    return True  
if __name__ == '__main__':
    while(True):
        N = int(input('Nhập số nguyên N > 0: '))
        if N > 0:
            break
        else:
            print('Nhập lại!')
    cnt = 1
    for i in range(10, N, 1):
        if checkNto(i) == True and checkNto(reversed(i)) == True and i != reversed(i):
            print(f'số emirp thứ {cnt} là: ', i)
            cnt += 1
    if cnt == 0:
        print('Không có số nào !')