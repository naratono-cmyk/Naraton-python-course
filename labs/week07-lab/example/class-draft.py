"""
programing ==> การเขียนโปรแกรม
2 types
1) structured programming ==> การเขียนโปรแกรมเชิงกระบวนการ ==> c , js , php , python
2) Object-oriented programming (oop) ==> การเขียนโปรแกรมเชิงวัตถุ ==> java , c# , python
"""
class ClassName:
    """Class docstring"""
    
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value
    
    def method_name(self):
        # Instance method
        return something


myObj = ClassName(parameters)
print(myObj.attribute)
resultFromMethod = myObj.method_name()


#ข้อมูลที่จำเป็นในการแก้ปัญหา
def __init__(self, parameters):
    # Constructor method
    self.attribute = value
    self.attribute2 = value
    self.attribute3 = value

#การกระทำเพื่อแก้ปัญหาต้องทำอย่างไรบ้าง
def method_name(self):
    # Instance method
    return something

def method_name2(self):
    return ...

#เริ่มต้นใช้งานคลาส ==> สร้างวัตถุจากคลาส
myObj = ClassName(parameters)
print(myObj.attribute)
resultFromMethod = myObj.method_name()
