import math

def get_phan_so(maSinhVien):  # hàm lấy phần (số) của mã sinh viên AT190128 ->190128
    limit = len(maSinhVien)
    ma = 0
    maSinhVien_reversed = maSinhVien[::-1]  
    for i in range(limit):
        if maSinhVien_reversed[i].isdigit():  # kiểm tra là số thì tính
            ma += 10 ** i * int(maSinhVien_reversed[i])  
    return int(ma) #trả về dạng số

def eratosthenes_segment(l, r):  # eratosthenes tạo mảng nguyên tố
    limit = r - l + 1
    primes = [1] * limit
    if l == 0:
        primes[0] = primes[1] = 0
    if l == 1:
        primes[1] = 0  # gán 2 thằng ban đầu là 0
    for i in range(2, int(math.sqrt(r) + 1)):
        start = max(i * i, (l + i - 1) // i * i)
        for j in range(start, r + 1, i):
            primes[j - l] = 0
    return [i for i in range(max(2, l), r + 1) if primes[i - l]]

def work(ma, primes):  # hàm lấy ra số nguyên tố gần nhất
    tmp = None  # tmp ban đầu
    min_distance = 1000000000 # cho min vô cùng lớn
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
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return 1 
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai vif kiem tra 0 roi
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b

if __name__ == '__main__':
    maSinhVien = input('Nhập vào mã sinh viên của bạn: ')
    ma = get_phan_so(maSinhVien)
    primes = eratosthenes_segment(2, 1000000)
    k = work(ma, primes)
    print(f"số nguyên tố gần với phần số của MSV = {ma} nhất là : ", k)
    a = int(input('Nhập vào SBD của bạn: '))
    # Từ số k tìm được tính a^k mod n (a = SBD)
    n = 123456
    result = modulo(a, k, n)
    print(f"Kết quả của {a} ^ {k} mod {n} = {result}")
    