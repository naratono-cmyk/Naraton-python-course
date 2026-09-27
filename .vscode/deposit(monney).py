def deposit(money):
    balance = 1000

    try:
        amount = float(money)

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

        balance += amount

    except ValueError as e:
        print("เกิดข้อผิดพลาด:", e)

    else:
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")


print("ยอดเงินเริ่มต้น: 1000 บาท")
money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")

deposit(money)