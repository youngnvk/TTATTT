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
    n = int(input('Nhap n: '))
    i = 1    
    while i <= n:
        sum = A * i * i + B * i + C
        if checknto(sum):
            print(i)
            break
        i += 1
    
    