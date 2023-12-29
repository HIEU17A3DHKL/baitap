# hàm kiểm tra số nguyên tố
def so_nguyen_to(n):
    flag = True
    if n < 1 :
        return False
    for i in range(2, n):
        if n % i:
            flag = Flase
    return flag

# hàm kiểm tra số chính phương

def so_chinh_phuong(n):
    if n < 1:
        return False
    for i in range(1, n+1):
        if i * i == n:
            return True
    return

# hàm kiểm tra số hoàn hảo

def so_hoan_hao(n):
    if n < 1:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0 :
            tong += i
    if tong == n:
        return True
    return

# hàm kiểm tra số lẻ

def so_le(n):
    if n < 0:
        return False
    for i in range(1, n+1):
        if n % 2 != 0:
            return True
    return


# hàm kiểm tra số chẵn
def so_chan(n):
    if n < 0:
        return False
    for i in range(1, n+1):
        if n % i == 0:
            return True
    return


# hàm kiểm tra số đối xứng
def so_doi_xung(n):
    if n < 0:
        return False
    if str(n) == str(n)[::-1]:
        return True
    return

# hàm tính ucln của hai số a, b
def ucln(a,b):
    uoc = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            uoc = i
    
    return int(uoc)

# hàm tính bcnn của hai số a, b

