print("N'Best") # ถ้าจะปริ้นข้อความต้องมี "" ด้วย
print(1) # ถ้าปริ้นตัวเลขไม่ต้องมี ""

print("\"") # ถ้าจะปริ้น " ต้องใช้ \"
print("\\") # ถ้าจะปริ้น \ ต้องใช้ \\

a = 5 # สร้างตัวแปรชื่อ a มาเก็บจำนวนเต็ม 5
print(a) # ปริ้นค่าที่อยู่ข้างในตัวแปร a
b = "IkQ" # สร้างตัวแปรชื่อ b มาเก็บข้อความ IkQ
print(b)

# เราสามารถถ่ายโอนค่าในตัวแปรหนึ่งไปอีกตัวแปรได้
c = 1
d = 2
print(c, d)
c = d
print(c, d)
d = 3
print(c, d)
c = 4
print(c, d)

text = input() # input เป็นคำสั่งในสั่งในการรับค่า
print(text)
IkQ = input("Please enter 1 number: ") # เราสามารถใส่ข้อความลงไปใน input ได้เพื่อให้ข้อความนั้นปริ้นออกมา

# รับค่าแบบเว้นบรรทัด
a = input()
b = input()
c = input()
print(a, b, c)

# รับค่าแบบ 1 บรรทัด มีเว้นวรรคคั่น
a, b, c = [x for x in input().split()]
print(a)
print(b)
print(c)

# การเขียน print โดยไม่ขึ้นบรรทัดใหม่
print(5, end = " ")
print(4)
