def cong(da_thuc_a, da_thuc_b):
    """
    Thực hiện phép cộng đa thức da_thuc_a và da_thuc_b trong trường hữu hạn.
    """
    do_dai = max(len(da_thuc_a), len(da_thuc_b))  # Độ dài của đa thức kết quả
    ket_qua = [0] * do_dai  # tạo mảng kết quả ban đầu là 0
    for i in range(do_dai):
        if i < len(da_thuc_a):
            ket_qua[i] ^= da_thuc_a[i]  # XOR từng hệ số của da_thuc_a
        if i < len(da_thuc_b):
            ket_qua[i] ^= da_thuc_b[i]  # XOR từng hệ số của da_thuc_b
    return ket_qua

def nhan(da_thuc_a, da_thuc_b):
    """
    Thực hiện phép nhân đa thức da_thuc_a và da_thuc_b trong trường hữu hạn.
    """
    do_dai = len(da_thuc_a) + len(da_thuc_b) - 1  # Độ dài của đa thức kết quả
    ket_qua = [0] * do_dai  # tạo mảng kết quả ban đầu là 0
    for i in range(len(da_thuc_a)):
        for j in range(len(da_thuc_b)):
            ket_qua[i + j] ^= da_thuc_a[i] * da_thuc_b[j]  # XOR từng tích của da_thuc_a[i] và da_thuc_b[j]
    return ket_qua

def lay_phan_du(da_thuc_a, da_thuc_mod):
    """
    Thực hiện phép lấy phần dư của đa thức da_thuc_a khi chia cho da_thuc_mod trong trường hữu hạn.
    """
    ket_qua = da_thuc_a[:]  # Sao chép đa thức da_thuc_a
    do_dai_mod = len(da_thuc_mod)
    for i in range(len(da_thuc_a) - 1, do_dai_mod - 2, -1):
        if ket_qua[i] == 1:
            for j in range(do_dai_mod):
                ket_qua[i - (do_dai_mod - 1 - j)] ^= da_thuc_mod[j]  # XOR với da_thuc_mod
    # Loại bỏ các hệ số 0 dư thừa
    while ket_qua and ket_qua[-1] == 0:
        ket_qua.pop()
    if not ket_qua:
        return [0]
    else:
        return ket_qua

def chia(da_thuc_a, da_thuc_b):
    """
    Thực hiện phép chia đa thức da_thuc_a cho da_thuc_b trong trường hữu hạn và trả về phần nguyên.
    """
    ket_qua = [0] * len(da_thuc_a)  # Đa thức ban đầu
    phan_du = da_thuc_a[:]  # Sao chép đa thức da_thuc_a để tính phần dư
    bac_da_thuc_b = len(da_thuc_b) - 1  # Bậc của đa thức da_thuc_b

    for i in range(len(da_thuc_a) - 1, bac_da_thuc_b - 1, -1):
        if phan_du[i] == 1:
            ket_qua[i - bac_da_thuc_b] = 1  # Cập nhật hệ số của phần nguyên
            for j in range(bac_da_thuc_b):
                phan_du[i - j] ^= da_thuc_b[j]  # XOR với da_thuc_b để cập nhật phần dư

    return ket_qua

def tim_nghich_dao(da_thuc_a, da_thuc_mod):
    """
    Tìm nghịch đảo của đa thức da_thuc_a trong trường hữu hạn với modulo da_thuc_mod bằng thuật toán Euclide mở rộng.
    """
    x0, x1 = [1], [0]  #tạo x0 = 1 và x1 = 0
    y0, y1 = [0], [1]  #tạo y0 = 0 và y1 = 1

    while len(da_thuc_mod) > 1 or da_thuc_mod[0] != 0:
        phan_nguyen = chia(da_thuc_a, da_thuc_mod)  # Tính phần nguyên
        phan_du = lay_phan_du(da_thuc_a, da_thuc_mod)  # Tính phần dư
        x = cong(x0, nhan(phan_nguyen, x1))  # Tính x
        y = cong(y0, nhan(phan_nguyen, y1))  # Tính y
        da_thuc_a, da_thuc_mod = da_thuc_mod, phan_du  # Cập nhật da_thuc_a và da_thuc_mod
        x0, x1 = x1, x  # Cập nhật x0, x1
        y0, y1 = y1, y  # Cập nhật y0, y1

    return x0

def chuoi_sang_nhi_phan(chuoi):
    """
    Chuyển đổi biểu thức đa thức từ chuỗi sang mảng nhị phân.
    """
    cac_thuoc = chuoi.split('+') 
    bac = 0
    for thuoc in cac_thuoc:
        if 'x^' in thuoc:
            bac_hien_tai = int(thuoc[thuoc.index('^') + 1:].strip())
        elif 'x' in thuoc:
            bac_hien_tai = 1
        else:
            bac_hien_tai = 0
        bac = max(bac, bac_hien_tai)

    da_thuc = [0] * (bac + 1)  # tạo mảng đa thức
    for thuoc in cac_thuoc:
        if 'x^' in thuoc:
            chi_so = int(thuoc[thuoc.index('^') + 1:].strip())
        elif 'x' in thuoc:
            chi_so = 1
        else:
            chi_so = 0
        da_thuc[chi_so] = 1  # Đánh dấu vị trí của x trong đa thức

    return da_thuc

def nhi_phan_sang_chuoi(da_thuc_nhi_phan):
    """
    Chuyển đổi đa thức từ mảng nhị phân sang biểu thức chuỗi.
    """
    ket_qua = []
    for i in range(len(da_thuc_nhi_phan) - 1, -1, -1):
        if da_thuc_nhi_phan[i] == 1:
            if ket_qua:
                ket_qua.append(" + ")  # Thêm dấu '+' 
            if i == 0:
                ket_qua.append("1") 
            elif i == 1:
                ket_qua.append("x") 
            else:
                ket_qua.append(f"x^{i}")  

    return ''.join(ket_qua)

if __name__ == "__main__":
    da_thuc_a_input = input("Nhập a(x): ").strip()  # Nhập đa thức a(x)
    da_thuc_g_input = input("Nhập g(x): ").strip()  # Nhập đa thức g(x)

    da_thuc_a = chuoi_sang_nhi_phan(da_thuc_a_input)  # Chuyển đổi đa thức a(x) từ chuỗi sang mảng nhị phân
    da_thuc_g = chuoi_sang_nhi_phan(da_thuc_g_input)  # Chuyển đổi đa thức g(x) từ chuỗi sang mảng nhị phân

    nghich_dao_a = tim_nghich_dao(da_thuc_a, da_thuc_g)  # Tìm nghịch đảo của a(x) trong trường hữu hạn với modulo g(x)

    print(f"a^-1(x) la", nhi_phan_sang_chuoi(nghich_dao_a))  # In ra nghịch đảo của a(x) dưới dạng chuỗi

