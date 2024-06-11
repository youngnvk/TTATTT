# Câu 24. Đặt S1, S2 là các mảng chứa giá trị bình phương của các số nguyên. 
# Hãy viết chương trình in ra số lượng tất cả các số nguyên tố nằm trong khoảng [a,b] 
# sao cho số này cũng là tổng của hai số x và y với x thuộc S1 và y thuộc S2. 
# Trong đó, a,b là các số được nhập từ bàn phím
# Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng [10,15] 
# chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9.
import math
def tao_mang_binh_phuong(n):
    a = [n] # 1 mang de chua
    for i in range(2, n + 1): #1 -> n
        a.append(i * i) # them i^2 vao mang
    return a
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def checkdieukien(a, b, n):
    for i in range(0, len(a)):
        for j in range(i + 1, len(b)):
            if a[i] + b[j] == n:
                return True
    return False   
if __name__== '__main__':
    a = int(input('nhập giá trị của a: '))
    b = int(input('nhập giá trị của b: '))
    S1 = tao_mang_binh_phuong(50) #thay số khác cũng dc
    S2 = tao_mang_binh_phuong(60) #thay số khác cũng dc
    for i in range(a, b + 1):
        if checknto(i) and checkdieukien(S1, S2, i):
             print(i)