def KMP(P, T):
    m = len(P)
    n = len(T)
    if m > n:
        return -1
    i = j = 0  # đặt con trỏ tại điểm ban đầu từ trái sang phải
    while i < n:  # đến khi chỉ số i vượt quá độ dài của chuỗi T
        if P[j] == T[i]:
            if j == m - 1:  # đã tới kí tự cuối
                return i - m + 1  # trả về vị trí khớp của chuỗi con trong T
            else:  # ngược lại
                i = i + 1  # duyệt tiếp
                j = j + 1
        else:
            f = failure(j, P[:j])
            i = i + j - f
            if f == -1:  # f[j] == 1 thì jnew = 0
                j = 0
            else:
                j = f  # gán jnew
    return -1  # Nếu không tìm thấy

def failure(k, P):
    if k <= 0:
        return -1
    x = 0
    for i in range(k):
        if P[:i] == P[-i:]:  # kiểm tra tiền tố = hậu tố
            x = i
    return x

if __name__=='__main__':
    T = input('Nhập chuỗi T : ')  
    P = input('Nhập chuỗi P : ')
    result = KMP(P, T)
    if result != -1:
        print(f'P có trong T bắt đầu từ vị trí {result}.')  
    else:
        print("Không có chuỗi S2 trong S1")
