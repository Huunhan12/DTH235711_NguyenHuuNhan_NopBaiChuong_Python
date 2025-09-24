count = 0   # biến đếm số *

for a in range(20, 100, 5):
    print('*', end='')
    count += 1   # mỗi lần in thì tăng đếm

print()  # xuống dòng
print("Tổng số dấu * đã in ra:", count)
