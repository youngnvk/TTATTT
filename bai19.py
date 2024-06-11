import math
def checknto(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    A = int(input('Nhập A: '))
    B = int(input('Nhập B: '))
    C = int(input('Nhập C: '))
    m = int(input('Nhập giá trị của m: '))
    l = int(input('Nhập giá trị của l(m < l): '))
    found = False
    for i in range(m, l + 1):
        sum = A * i * i + B * i + C
        if checknto(sum):
            print(i)
            found = True
    if not found:
        print('Không tìm thấy')
    
