import math

def count1(N):
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
def count2(N):
    limit = int(math.sqrt(N)) + 1
    cnt = 0
    for i in range(1, limit):
        if N % i == 0:
            cnt += 1
            if i * i != N:
               cnt += 1
    return cnt
if __name__ == "__main__":
    N = int(input("Nhập giá trị N: "))
    k = count1(N)
    s = count2(N)
    print("Số ước nguyên tố của số N là : ", k)
    print("Số ước của số N là : ", s)
