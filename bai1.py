import math
def Q_prime(n):
    cnt = 0
    ok = False
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                cnt += 1  # Trường hợp n là số chính phương
            else:
                cnt += 2  # Cặp ước (i, n // i)
    if cnt == 4:
        ok = True
    return ok
if __name__ == '__main__':
    while(True):
        n = int(input('Nhập 1 số N cho trước: '))
        if n > 0:
            break
        else:
            print('mời bạn nhập lại!')
    print(f'các số Q-Prime thỏa mãn là: ')
    cnt = 1
    for i in range(2, n + 1):
        ok = Q_prime(i)
        if ok == True:
            print(f"số thứ {cnt}: {i}")
            cnt += 1
    if cnt == 10:
        print('Không có số nào !')
