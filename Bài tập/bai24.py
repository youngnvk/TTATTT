import math
def tao_mang_binh_phuong(n): #Hàm tạo mảng bình phương S1, S2
    A = [] # 1 mang de chua  phần tử
    for i in range(1, n + 1): #1 -> n
        A.append(i * i) # them i^2 vao mang
    return A
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def checkdieukien(S1, S2, n): #hàm kiểm tra điều kiện bài toán
    for i in range(0, len(S1)):
        for j in range(0, len(S2)): #để bỏ TH 2 số giống nhau và giảm số lần lặp
            if S1[i] + S2[j] == n:
                return True
    return False   
if __name__== '__main__':
    a = int(input('nhập giá trị của a: '))
    b = int(input('nhập giá trị của b: '))
    S1 = tao_mang_binh_phuong(50) #thay số khác cũng dc
    S2 = tao_mang_binh_phuong(60) #thay số khác cũng 
    cnt = 0
    for i in range(a, b + 1):
        if checknto(i) and checkdieukien(S1, S2, i):
           cnt += 1
           print(i)
    print('Số lượng số nguyên tố thỏa mãn yêu cầu bài toán là : ', cnt)         
             
             
#Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng [10,15]
# chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9.