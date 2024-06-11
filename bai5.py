#Câu 5. Viết chương trình tính tổng của các số nguyên tố
# nằm trong khoảng [A, B] với A, B nhập vào từ bàn phím.
import math
def sum_primes(l, r):
    limit = r - l + 1
    # Giả sử tất cả các số là nguyên tố ban đầu 
    primes = [1] * limit
    if l < 2:
        primes = [0, 0]  # 0 và 1 không phải số nguyên tố:
    for i in range(2, int(math.sqrt(r)) + 1):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
            primes[j - l] = 0  # Bỏ đánh dấu các bội số của i 
    sum = 0       
    for i in range(max(2, l), r + 1):
        if (primes[i - l]):
            sum += i
    return sum
if __name__== '__main__':
    l = int(input('Nhập giá trị của l: '))
    r = int(input('Nhập giá trị của r: '))
    print(sum_primes(l, r))
    