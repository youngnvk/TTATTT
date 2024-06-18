import math
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def find(N):
    l = 10**(N - 1)
    r = 10**N
    for num in range(l, r):
        if isprime(num):
            print(num)
if __name__ == '__main__':
   while(True):
        N = int(input('Nhập N từ bàn phím 2 <= N <= 10: '))
        if 2 <= N <= 10:
            print(f"các số nguyên tố có {N} chữ số là: ")
            find(N)
        else:
            print("Giá trị của N phải nằm trong khoảng từ 2 đến 10.")
            print('Mời nhập lại!')