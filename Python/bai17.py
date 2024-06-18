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
    x = 1    
    while True:
        sum = A * x * x + B * x + C
        if checknto(sum):
            print("Nghiệm x nhỏ nhất để tổng Ax^2 + Bx + C là số nguyên tố là:", x)
            break
        x += 1
    
    