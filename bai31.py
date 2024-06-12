import math

def get_phan_so(maSinhVien):  # hàm lấy phần số mã sinh viên
    limit = len(maSinhVien)
    ma = 0
    maSinhVien_reversed = maSinhVien[::-1]  # reverse the string
    for i in range(limit):
        if maSinhVien_reversed[i].isdigit():  # kiểm tra là số
            ma += 10 ** i * int(maSinhVien_reversed[i])  # calculate the reversed number
    return int(ma)

def eratosthenes_segment(l, r):  # eratosthenes tạo mảng nguyên tố
    limit = r - l + 1
    primes = [1] * limit
    if l == 0:
        primes[0] = 0
    if l == 1:
        primes[1] = 0  # gán 2 thằng ban đầu là 0
    for i in range(2, int(math.sqrt(r) + 1)):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
            primes[j - l] = 0
    return [i for i in range(max(2, l), r + 1) if primes[i - l]]

def work(ma, primes):  # hàm lấy ra số gần nhất
    tmp = None  # tmp ban đầu
    min_distance = float('inf')  # cho min vô cùng lớn
    for i in primes:
        distance = abs(ma - i)
        if distance < min_distance:
            min_distance = distance
            tmp = i
        elif distance == min_distance:
            tmp = min(i, tmp)  # Nếu khoảng cách bằng nhau, chọn số nhỏ hơn
    return tmp  # trả về số cần tìm

def bin(n):  # Chuyển đổi số nguyên sang dạng nhị phân
    arr2 = []
    cnt = 0
    while n != 0:
        r = n % 2
        arr2.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr2

def modulo(a, k, n):  # Hàm tính lũy thừa modulo bằng phương pháp bình phương và nhân
    cnt, arr2 = bin(k)
    b = 1
    if k == 0:
        return 1  # 0^0 là 1 theo định nghĩa
    A = a
    if arr2[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai
        A = (A * A) % n
        if arr2[i] == 1:
            b = (A * b) % n
    return b

if __name__ == '__main__':
    maSinhVien = input('Nhập vào mã sinh viên của bạn: ')
    ma = get_phan_so(maSinhVien)
    n = 123456
    a = int(input('Nhập vào SBD của bạn: '))
    # giả sử giới hạn phần check số nguyên tố trong khoảng 2->100000
    primes = eratosthenes_segment(2, 100000)
    k = work(ma, primes)
    # Từ số k tìm được tính a^k mod n (a = SBD)
    result = modulo(a, k, n)
    print(result)
    
    
    

