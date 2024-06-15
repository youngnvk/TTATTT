import random
import math

def Phepcong(a, b):
    C = [0] * (len(a) + 1) 
    for i in range(len(a)):
        if i < len(b):  # Check if b has enough elements
            C[i] = (a[i] + b[i]) % 2
        else:
            C[i] = a[i] % 2 # Default to a[i] if b is shorter
    return C
def Phepchia(d, g):
    x = len(d) - 1
    y = len(g) - 1
    while x >= y:
        q = [0] * (len(d) - len(g) + 1)
        q[x - y] = 1  # Set the correct quotient coefficient to 1
        d = Phepcong(d, Phepnhan(q, g))  # Perform polynomial subtraction properly
        x = - 1 # Update degree of remainder
    return d

def Phepnhan1(a, b):
    deg_a = len(a)
    deg_b = len(b)
    d = [0] * (deg_a + deg_b - 1)
    for i in range(deg_a):
        for j in range(deg_b):
            d[i + j] = (d[i + j] + a[i] * b[j]) % 2
    while d and d[0] == 0:
        d.pop(0)  # Remove leading zeros
    return d

def Phepnhan(a, b):
    deg_a = len(a)
    deg_b = len(b)
    d = [0] * (deg_a + deg_b - 1)
    for i in range(deg_a):
        for j in range(deg_b):
            d[i + j] = (d[i + j] + a[i] * b[j]) % 2
    return d

if __name__ == '__main__':
    a1 = [0, 1, 0, 1]
    g = [1, 0, 1, 1]  
    b = [0, 1, 1, 1]
    
    # Perform polynomial multiplication
    d = Phepnhan(a1, b)
    print("Product of a(x) and b(x):", d)
    
    # Perform polynomial division
    remainder = Phepchia(d, g)
    print("Remainder of division:", remainder)
