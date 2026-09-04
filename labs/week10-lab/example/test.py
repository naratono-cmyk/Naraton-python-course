
#เขียนโปรแกรมเพื่อนับจำนวนอักขระในข้อความ
#รับอักขระที่สนใจจากผู้ใช
#รับข้อความจากผู้ใช้

#insert the text : Kasetsart sriracha
#character to find: r
# 3 letter 'r' found in 'kasetsart sriracha'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")

#-----------------------------------------------------------------------------------------------#

#เขียนโปรแกรมตรวจสอบความปลอดภัยของรหัสผ่าน
#ต้องมีขั้นต่ำความยาว 8 ตัว รวมตัวเลข ตัวอักษร และอักขระพิเศษ


password = input("Insert your password: ")
lenght = len(password)
check = password.isalnum()     #ตรวจสอบว่ามีตัวอักษรและตัวเลขหรือไม่

if lenght >= 8 and check == False:
    print("Your password is strong.")
else:
    print("Your password is notstrong.")
 

