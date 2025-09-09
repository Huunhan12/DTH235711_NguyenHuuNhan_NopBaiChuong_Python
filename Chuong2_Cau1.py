# Chuong2_Cau1.py: Tính chu vi và diện tích hình tròn
import math
try:
 r=float(input("Mời bạn nhập bán kính hình tròn:"))
 cv=2*math.pi*r
 dt=r**2
 print("Chu vi =",cv)
 print("Diện tích=",dt)
except:
 print("Lỗi rồi!")
