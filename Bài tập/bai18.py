import math
def Phepcong(A, B, W, t):
    C = [0] * t # Tạo mảng chứa t phần tử ban đầu giá trị 0
    # Tạo giá trị bit nhớ e
    e = 0
    for i in range(t - 1, -1, -1):
        x = 2 ** W
        C[i] = A[i] + B[i] + e #công thức
        if C[i] >= x:
            e = 1
            C[i] = C[i] % x
        else:
            e = 0
    return e, C
def mang_sang_so(F, W, A): #hàm mảng sang số
    m = math.ceil(math.log2(F))
    t = math.ceil(m / W)
    result = 0
    for i in range(0, t):
        x = 2 **((t - i - 1) * W)
        result += A[i] * x       
    return result
def so_sang_mang(F, W, a): #hàm số sang mảng
    list = []
    m = math.ceil(math.log2(F)) # số bit cần biểu diễn
    t = math.ceil(m / W) # số lượng phần tử trong mảng đầu ra
    for i in range(1, t + 1):
        x = 2 ** ((t - i) * W)
        b = a // x
        a = a % x
        list.append(b)
    return list
if __name__=='__main__':
    F = int(input('Nhập F : '))
    W = int(input('Nhập W: '))
    m = math.ceil(math.log2(F))
    t = math.ceil(m / W) 
    A = int(input('Nhập số A: '))
    A = so_sang_mang(F, W, A) #chuyển số sang mảng A
    B = int(input('Nhập số B: '))
    B = so_sang_mang(F,W, B) #chuyển số sang mảng B
    result = [0] * 2
    result = Phepcong(A, B, W, t) #cộng 2 mảng A B
    print("Kết quả trên dạng mảng:", result[1]) # in kết quả dạng mảng
    a =  mang_sang_so(F, W, result[1])
    print("Kết quả trên dạng số:", a) #in kết quả dạng số
