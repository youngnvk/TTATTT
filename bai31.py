import math
def get_phan_so(maSinhVien): #hàm lấy phần số mã sinh viên
    limit = len(maSinhVien)
    ma = 0
    masinhvien2.reversed()
    for i in range(limit):  
        if maSinhVien2[i].isdigit(): # kiểm tra là số
            ma += 10 ** tmp  * int(maSinhVien2[i])
    return int(ma)
def eratosthenes_segment(l, r): #eratosthenes tạo mảng nguyên tố
    limit = r - l + 1
    primes = [1] * limit
    if l < 2:
        primes[0] = primes[1] = 0 #gán 2 thằng ban đầu là 0
    for i in range(2, int(math.sqrt(r) + 1)):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
                primes[j - l] = 0      
    return [i for i in range(max(2, l), r + 1) if primes[i - l]]
def work(ma, primes): #hàm lấy ra số gần nhất
    tmp = None #tmp ban đầu
    min_distance = float('inf') #cho min vô cùng lớn
    for i in primes:
        distance = abs(ma - i)
        if distance < min_distance:
            min_distance = distance
            tmp = i
        elif distance == min_distance:
            #> lần 2
            tmp = min(i, tmp) # Nếu khoảng cách bằng nhau, chọn số nhỏ hơn
    return tmp #trả về số cần tìm
def modulo(a, k, m): #hàm tính modulo
    if a % m == 0:
        return 0
    b = 1
    a = a % m
    while(k != 0):
        if k  % 2 == 1:
            b = (b * a) % m
        k = k // 2
        a = (a * a) % m
    return b                
if __name__ == '__main__':
    maSinhVien = input('Nhập vào mã sinh viên của bạn: ')
    ma = get_phan_so(maSinhVien)
    n = 123456
    a = int(input('Nhập vào SBD của bạn : '))
    #giả sử giới hạn phần check số nguyên tố trong khoảng 2->100000 => 
    primes = eratosthenes_segment(2, 100000)
    k = work(ma, primes)
    #Từ số k tìm được tính a^k mod n (a = SBD)
    result = modulo(a, k, n)
    print(result)
    
    
    
    

