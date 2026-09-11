units = int(input("กรอกจำนวนหน่วยไฟฟ้า:"))

def calculate_electricity_cost(units):

    if units > 200:
       cost = 125.0 + 150.00 + 350.00
       ((units-200)*4.00)+25
       print("1-50 หน่วย: 125.00 บาท")
       print("51-100 หน่วย: 150.00 บาท")
       print("101-200 หน่วย: 350.00 บาท")
       print(f"201-{units} หน่วย: {(units-200)*4.00} บาท")
       print("ค่าบริการ: 25.00 บาท")
       print("รวมค่าไฟทั้งสิ้น:", cost, "บาท")

    elif units > 100:
     cost = (50 * 2.50) + (50.0 * 3.00)+((units-100) * 3.50) + 25
     print("51-100 หน่วย: 150.00 บาท")
     print(f"101-{units} หน่วย: {(units-100)*3.50} บาท")
     print("ค่าบริการ: 25.00 บาท")
     print("รวมค่าไฟทั้งสิ้น:", cost, "บาท")


    elif units >50:
     cost = 125.0 + ((units - 50) * 3.00) + 25
     print("1-50 หน่วย: 125.00 บาท")
     print(f"51-{units} หน่วย : {(units - 50) * 3.00} บาท")
     print("ค่าบริการ: 25.00 บาท")
     print("รวมค่าไฟทั้งสิ้น:", cost, "บาท")
                 
    elif units >=0:
      cost = units * 2.50 + 25
      print("1-50 หน่วย: 125.00 บาท")
      print("51-100 หน่วย: 150.00 บาท")
      print("ค่าบริการ: 25.00 บาท")
      print("รวมค่าไฟทั้งสิ้น:", cost, "บาท")
    else:
        print("จำนวนไฟฟ้าต้องไม่ติดลบ")
 
while True:
    print("===โปรแกรมหน่วยค่าไฟฟ้า===")
    print("1) คำนวณค่าไฟฟ้า")
    print("2) ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
       units = int(input("กรอกจำนวนหน่วยไฟฟ้า:"))
       calculate_electricity_cost(units)
    elif choice == "2":
       break
    else:
        print("หากเลือกเมนูไม่ถูกต้อง ให้เลือกเมนูไม่ถุกต้อง")
