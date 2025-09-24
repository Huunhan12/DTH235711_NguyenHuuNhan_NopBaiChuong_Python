'''
Trường hợp (a) i=3, j=5, k=7
Kiểm tra i < j → 3 < 5 → True
Trong nhánh đó: kiểm tra j < k → 5 < 7 → True
→ i = j = 5
Kết quả: i=5, j=5, k=7

Trường hợp (b) i=3, j=7, k=5
i < j → 3 < 7 → True
Kiểm tra j < k → 7 < 5 → False
→ j = k = 5
Kết quả: i=3, j=5, k=5

Trường hợp (c) i=5, j=3, k=7
i < j → 5 < 3 → False
Sang nhánh else: kiểm tra j > k → 3 > 7 → False
→ i = k = 7
Kết quả: i=7, j=3, k=7

Trường hợp (d) i=5, j=7, k=3
i < j → 5 < 7 → True
Kiểm tra j < k → 7 < 3 → False
→ j = k = 3
Kết quả: i=5, j=3, k=3

Trường hợp (e) i=7, j=3, k=5
i < j → 7 < 3 → False
Sang nhánh else: kiểm tra j > k → 3 > 5 → False
→ i = k = 5
Kết quả: i=5, j=3, k=5

Trường hợp (f) i=7, j=5, k=3
i < j → 7 < 5 → False
Sang nhánh else: kiểm tra j > k → 5 > 3 → True
→ j = i = 7
Kết quả: i=7, j=7, k=3
'''