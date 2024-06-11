import math
def T_prime1(n, A):
    cnt = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                cnt += 1  # Trường hợp n là số chính phương
            else:
                cnt += 2  # Cặp ước (i, n // i)
    if cnt == 4:
        A.append(n)
if __name__ == '__main__':
    n = int(input('Nhập 1 số N cho trước: '))
    if n > 0:
        A = []
        for i in range(2, n + 1):
            T_prime1(i, A)
        print(A)
