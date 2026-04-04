# Đọc file
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Tách từ
words = content.split()

# Tạo dictionary để đếm
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

# In kết quả
print(count)