a = 0
count = 0   # biến để đếm số dấu *
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
            count+=1
        b += 1
     
    print()
    a += 1
    print()          # xuống dòng
print("Tổng số dấu * đã in ra:", count)
