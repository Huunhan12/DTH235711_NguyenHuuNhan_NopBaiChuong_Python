for i in range(1,11):           # i chạy từ 1 → 10
    for j in range(2,10):       # j chạy từ 2 → 9
        line = "{0}*{1:>2}={2:>2}".format(j, i, i*j)
        print(line, end='\t')   # in ra cùng 1 hàng, cách nhau tab
    print()                     # xuống dòng sau mỗi i
  