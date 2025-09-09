# Chuong2_Cau2.py: Chuyển đổi giây sang giờ, phút, giây
t=int(input("Nhập số giây:"))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
print(hour," Giờ","\n",minute," Phút","\n",second," Giây")