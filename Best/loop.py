# # check condition -> True -> statement -> check condition -> True -> statement -> ... -> False -> out
# # while condition:
# #     statement

a = 1
sum = 0

while a <= 10:
    sum = sum + a
    print(sum, end = " ")
    a = a + 1
    
# # ----------------------------------------------------------------

# วนลูป range ครั้ง
# for i in range():
#     statement

n = int(input())

# วนลูป n โดยที่ i = 0, 1, 2, ..., n - 1
# ใน range ตัวที่แรกคือ i ต้องน้อยกว่า
for i in range(n):
    print(i)

# วนลูป n - 5 ครั้ง โดยที่ i = 5, 6, 7, ..., n - 1
# ใน range ตัวแรกคือ ตัวเริ่ม i
# ใน range ตัวที่สองคือ i ต้องน้อยกว่า
for i in range(5, n):
    print(i)

# วนลูป i = 1, 3, 5, ..., 9
# ใน range ตัวแรกคือ ตัวเริ่ม i
# ใน range ตัวที่สองคือ i ต้องน้อยกว่า
# ใน range ตัวที่สามคือ จำนวนที่ i เพิ่มแต่ละครั้ง
for i in range(1, 10, 2):
    print(i)












