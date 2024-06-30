# data -> ข้อมูล, type -> ชนิด
# datatype -> ชนิดของข้อมูล

# datatype: int (ย่อมาจาก integer)
# จำนวนเต็ม เช่น 1, 5, 0, -8
a = 13
# datatype: float
# ทศนิยม เช่น 3.8, -2.5, 1.0
b = -2.05
# datatype: string
# ข้อความ เช่น "a", "-3", "string", "print"
c = "N'Best"
d = input()

# string สามารถบวกกันได้ และสามารถคูณกับ int ได้
print("3" + "4") # "3" + "4" -> "34"
print(10 * "Nabc")

# การเปลี่ยน datatype
# เราจะใส่ int(), float() หรือ str() ล้อมรอบ data
e = float(a)
f = int(-2.55)
g = str(b)
