import random
def fermat(a, n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        if modulo(a, n-1, n) != 1: # modulo_power(a, n-1, n)
            return False
        return True
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
if __name__=='__main__':
    n = int(input("Nhập giá trị của n: "))
    array_random = [random.randint(1, 100) for i in range(n)]
    print("Mảng random n phần tử là: ", array_random)
    print("Các số nguyên tố trong mảng trên là : ")
    for i in range(len(array_random)):
        a = random.randint(2, n - 2)
        if fermat(a, array_random[i]):
                print(array_random[i], end=' ')
