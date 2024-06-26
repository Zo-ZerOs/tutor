# data = ข้อมูล
# type = ชนิด
# datatype = ชนิดของข้อมูล

# 3 ชนิดที่ใช้บ่อยๆ
# 1) int (integer = จำนวนเต็ม) -> 5 10 -2 0 -89
# 2) float (จำนวนจริง) -> 2.38 -5.6 3.0
# 3) string (ข้อความ) -> "I love pizza" "dog is cat"

a = 3 # int
b = -10.7 # float
c = "1" # string
d = "My grade is 4.00" # string

# e = input() # string
# f = input()
# print(e - f) is error!!! เพราะ string ลบกันไม่ได้

# การเปลี่ยน datatype
print(float(a)) # เปลี่ยนจาก int เป็น float เติม .0
print(int(b)) # เปลี่ยนจาก float เป็น int เอาทศนิยมทิ้ง
print(int(c)) # เปลี่ยนจาก string เป็น int หรือ float    string นั้นๆ ต้องเป็นตัวเลข
