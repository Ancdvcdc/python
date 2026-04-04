n = int(input("Nhập số n: "))
i = 0
tong = 0

while i < n:
    if i % 2 == 0:
        tong += i
    i += 1

print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)