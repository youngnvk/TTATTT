import math

import math
def boyer(P, T):
    m = len(P)
    n = len(T)
    if m > n:
        return -1
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
    return -1 #không tìm thấy     
def check_last_P(k, P): #hàm kiểm tra vị trí cuối cùng trong P
    vt = -1 #không có kí tự thì trả về vị trí là -1
    for i in range(0, len(P)):
        if k == P[i]:
            vt = i #cứ chạy đến cuối sẽ ra vị trí đầu tiên
    return vt  
def last_occurrence(k, P):
    vt = -1
    for i in range(0, len(P)):
        if k == P[i]:
            vt = i
    return vt

if __name__=='__main__':
    vanban1 = input('Nhập chuỗi mẫu T: ')
    vanban2 = input('Nhập chuỗi văn bản P: ')
    result = boyer(vanban2, vanban1)
    result2 = int(boyer(vanban2, vanban1))
    if result != -1:
        for pos in result:
            print(pos)
    else:
        print("")
