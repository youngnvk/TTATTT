def Phepcong(a, b):
    # Đảm bảo cả hai đa thức có cùng độ dài
    length = max(len(a), len(b))
    a = [0] * (length - len(a)) + a
    b = [0] * (length - len(b)) + b
    C = [(a[i] + b[i]) % 2 for i in range(length)]
    return C

def Phepnhan(a, b):
    deg_a = len(a)
    deg_b = len(b)
    d = [0] * (deg_a + deg_b - 1)
    for i in range(deg_a):
        for j in range(deg_b):
            d[i + j] = (d[i + j] + a[i] * b[j]) % 2
    return d
def Phepchia(d, g):
    x = len(d) - 1
    y = len(g) - 1
    while x >= y:
        q = [0] * (len(d) - len(g) + 1)
        q[x - y] = d[x]
        d = Phepcong(d, Phepnhan(q, g))
        while len(d) > 0 and d[0] == 0:
            d.pop(0)
        x -= 1
    return d[-4:]    
if __name__ == '__main__':
    a = [1, 0, 1, 0]  # 1 + x^2
    g = [1, 0, 1, 1]  # 1 + x + x^3
    b = [1, 1, 1, 0]  # 1 + x + x^2
    
    # Tính tích của a(x) và b(x)
    d = Phepnhan(a, b)
    print("Tích của a(x) và b(x):", d)
    
    # Tính thương và dư của phép chia
    quotient, remainder = Phepchia(d, g)
    print("Thương của phép chia:", quotient)
    print("Dư của phép chia:", remainder)
