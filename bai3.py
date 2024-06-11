import math
def phantichNto(N, A):
    limit = int(math.sqrt(N)) + 1
    for i in range(2, limit, 1):
        if N % i == 0:
            A.append(i)
            while(N % i == 0):
                N //= i
    if (N != 1):
        A.append(N)
def phantich(N, B):
    limit = int(math.sqrt(N)) + 1
    for i in range(1, limit, 1):
        if N % i == 0:
            B.append(i)
            if i * i != N:
                B.append(N // i)
if __name__=="__main__":
    N = int(input("Nhập giá trị N: "))
    A = []
    B = []
    phantichNto(N, A)
    phantich(N, B)
    q = sum(A)
    k = len(A)
    p = sum(B)
    s = len(B)
    result = N + p + s - q - k
    print("Kết quả của biểu thức N+p+s-q-k với N =", N, "là:", result)
    
    