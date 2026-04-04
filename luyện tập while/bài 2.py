n = int(input("Nhập số n: "))
i = 1
giai_thua = 1

while i <= n:
    giai_thua *= i
    i += 1

print(f"Giai thừa của {n} là:", giai_thua)