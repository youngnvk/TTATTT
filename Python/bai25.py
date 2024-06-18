import math
import itertools
def eratosthenes(n): #hàm eratosthenes sàng
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
def test(n, m):
    primes = eratosthenes(n)
    for a in itertools.combinations(primes, m): #combination để tạo ra tất cả các (mảng)bộ trong mảng có m kí tự có thể tạo ra của primes
        if sum(a) == n:
            return a
    return None
if __name__ == "__main__":
    while True:
        n = int(input("Nhập giá trị của N: "))
        m = int(input("Nhập giá trị của M: "))
        if 1 <= n <= 10000 and 2 < m <= 100:
            break
        else:
            print("Vui lòng nhập lại N và M!")
    Result = test(n, m)
    #in số
    if Result:
        print(f"Số {n} có thể phân tích thành tổng của {m} số nguyên tố là: {n} = ", end="")
        cnt = 0
        for i in Result:
            if cnt == m - 1:
                print(i)
            else:
                print(i, end=" + ")
            cnt += 1               
    else:  # không trả về result => sai k thể phân tích
        print(f"Số {n} không thể phân tích thành tổng của {m} số nguyên tố.")
