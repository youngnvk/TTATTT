import random
def fermat(a, n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        if modulo_power(a, n-1, n) != 1: # modulo_power(a, n-1, n)
            return False
        return True
def modulo_power(a, k, m): #nhân bình phương có lặp
    if a % m == 0:
        return 0 
    b = 1
    a = a % m 
    while k > 0:
        if k % 2 == 1:
            b = (b * a) % m
        k = k // 2
        a = (a * a) % m
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
