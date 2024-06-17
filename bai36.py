import math
def boyer(P, T):
    if len(P) > len(T):
        return False
    m = len(P)
    n = len(T)
    i = j = m - 1
    while(i < n):
        if P[j] == T[i]:
            if j == 0:
                return i #trả về vị trí của điểm giống nhau trong T để in ra
            else: #kiểm tra tiếp theo
                i = i - 1
                j = j - 1
        else:#không giống nên nhảy
            #tiền xử lý
            i = i + m - min(j, 1 + check_last_P(T[i],P)) #cập nhật vị trí i
            j = m - 1 #cập nhật lại j
    return False #không tìm thấy     
def check_last_P(k, P): #hàm kiểm tra vị trí cuối cùng trong P
    vt = -1 #không có kí tự thì trả về vị trí là -1
    for i in range(0, len(P)):
        if k == P[i]:
            vt = i #cứ chạy đến cuối sẽ ra vị trí đầu tiên
    return vt   
if __name__=='__main__':
    S1 = "a pattern matching algorithm"
    S2 = "rithm"
    TEST = boyer(S2, S1)
    if TEST == False:
        print('P không có trong T.')
    else:
        print(f'P có trong T bắt đầu từ vị trí {TEST}.')  
