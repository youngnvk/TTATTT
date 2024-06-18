import math
def countuocnguyento(N):
    limit = int(math.sqrt(N)) + 1
    cnt = 0
    for i in range(2, limit):
        if N % i == 0:
            cnt += 1
            while N % i == 0:
                N //= i
    if N != 1:
       cnt += 1
    return cnt
def countuoc(N):
    limit = int(math.sqrt(N)) + 1
    cnt = 0
    for i in range(1, limit):
        if N % i == 0:
            cnt += 1
            if i * i != N:
               cnt += 1
    return cnt
if __name__ == "__main__":
    while(True):
        N = int(input('Nhập n: '))
        if N > 0:
            break
        else:
            print('Nhập lại!')
    k = countuocnguyento(N)
    s = countuoc(N)
    print(f"Số ước nguyên tố của số {N} là : ", k)
    print(f"Số ước của số {N} là : ", s)
