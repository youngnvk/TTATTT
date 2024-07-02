import random
import math
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def random_array(n, l, r):
    arr = [n]
    for i in range(n):
        a = random.randint(l, r)
        if a not in arr: #để cho các phần tử  trong mảng không giống nhau
            arr[i] = random.randint(l, r)   
    return arr     
if __name__=='__main__':
    while(True):
        n = int(input('Nhập giá trị(số lượng phần tử trong mảng) n > 0: '))
        if n > 0:
            break
        else:
            print('Nhập lại n')
    while(True):
        l = int(input('Nhập giá trị l của khoảng sinh : '))
        if l > 0:
            break
        else:
            print('Nhập lại l')
    while(True):
        r = int(input('Nhập giá trị r của khoảng sinh : '))
        if r > l:
            break
        else:
            print('Nhập lại r')
    array_random = random_array(n, l, r)
    print(f'Mảng sinh ngẫu nhiên {n} phần tử là : ', array_random)
    print("Các số nguyên tố trong mảng trên là : ")
    cnt = 1
    for i in range(n):
        if checknto(array_random[i]):
                print(f'số nguyên tố thứ {cnt} là :', array_random[i])
                cnt += 1
    if cnt == 1:
        print('Không có số nào !')