
def uoc(n):
    cac_uoc = []
    count = 0
    tong = 0
    if n < 0:
        return False
    for i in range(1, n+1):
        if n % i == 0:
            cac_uoc.append(i)
            count += 1
            tong += i
    return cac_uoc, count, tong

n = int(input("nhập vào số nguyên n: "))
cac_uoc, count, tong = uoc(n)
print(f"các ước của {n} là {cac_uoc}")
print(f"{n} có {count} ước")
print(f"tổng các ước của {n} là {tong}")

def so(n):
    cac_so = []
    for i in range(1000, 2001):
        if i % 3 == 0 and i % 2 != 0:
            cac_so.append(i)
    return cac_so
cac_so = so(n)
print(f"các số trong khoảng từ (1000, 2000) là {cac_so}")