import random

def choi_game():
    so_may = random.randint(1, 100)  # Máy chọn ngẫu nhiên số từ 1 đến 100
    so_lan_doan = 0
    gioi_han = 7

    print("Game Đoán Số (1..100)")
    print("Bạn chỉ có tối đa 7 lần đoán!")

    while so_lan_doan < gioi_han:
        try:
            doan = int(input(f"Lần đoán {so_lan_doan+1}: Nhập số bạn đoán (1..100): "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
            continue

        so_lan_doan += 1

        if doan == so_may:
            print(f"Chính xác! Bạn đã đoán đúng số {so_may} trong {so_lan_doan} lần.")
            break
        elif doan < so_may:
            print("ố bạn đoán nhỏ hơn số của máy.")
        else:
            print("Số bạn đoán lớn hơn số của máy.")
    else:
        print(f"Bạn đã thua! Số đúng là {so_may}.")

    # Hỏi người chơi có chơi tiếp không
    tiep_tuc = input("Bạn có muốn chơi tiếp không? (c/k): ").lower()
    if tiep_tuc == "c":
        choi_game()
    else:
        print("Cảm ơn bạn đã chơi!")

# Gọi hàm để bắt đầu game
choi_game()
