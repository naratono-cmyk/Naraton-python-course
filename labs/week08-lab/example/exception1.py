try:
    num1 = float(input("กรอกตัวเลขตัวที่ 1: "))
    num2 = float(input("กรอกตัวเลขตัวที่ 2: "))
    operator = input("กรอกเครื่องหมาย (+, -, *, /): ")

    result = 0
    if operator == "+":
     result = num1 + num2
    elif operator == "-":
     result = num1 - num2
    elif operator == "*":
     result = num1 * num2
    elif operator == "/":
     result = num1 / num2
    else:
     raise ValueError("กรุณากรอกเครื่องหมาย +, -, *, / เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")