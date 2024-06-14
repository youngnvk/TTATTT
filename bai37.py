def KMP(P, T):
    m = len(P)
    n = len(T)
    if m > n : 
        return False
    i = j = 0 # đặt con trỏ tại điểm ban đầu từ trái sang phải
    while(i < n):
        if P[j] == T[i]:
            if j == m - 1: #đã tới kí tự cuối
                return i - m + 1 #trả về vị trí trùng nhau 
            else:
                i = i + 1
                j = j + 1
        else:
            i = i + j - failure(j, P)
            if failure(j, P) == -1:
                j = 0
            else:
                j = failure(j, P)
def failure(k,P):
    #print("k=",k)
    if k <= 0:
        return -1
    A=P[:k]  
    #print("tiền tố A=",A)
    x=0
    for i in range(k):
        if A[:i] == A[-i:] : # kiểm tra tiền tố = hậu tố
            x += 1
    return x        
S1 = "a pattern matching algorithm"
S2 = "rithm"
print(KMP(S2, S1))
    
    