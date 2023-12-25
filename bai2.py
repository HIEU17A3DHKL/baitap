n = int(input("nhập vào một số nguyên: "))
A = 0
for i in range(1, n+1):
    A += i
print(A)

B = 0
for i in range(1, n+1):
    if i % 2 == 0:
        B += i
print(B)

C = 0
for i in range(1, n+1):
    if i % 2 != 0:
        C += i
print(C)

D = 1
for i in range(1, n+1):
    D *= i
print(D)

E = 1
for i in range(1, n+1):
    if i % 3 == 0:
        E *= i
print(E)

F = 0
def so_nguyen_to(n):
    if n < 2:
        return False
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag
for i in range(1, n+1):
    if so_nguyen_to(i):
        F += i
print(F)


E = 0
for i in range(1, n+1):
    E += ((-1)** i)/i
print(E)

H = 0
for i in range(1, n+1):
    H += i**0.5
print(H)

