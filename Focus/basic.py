# output การแสดงผล
print("IkQ")    # การแสดงผลข้อความ
print("1")

# comment

# Variable (ตัวแปร)# output การแสดงผล
print("IkQ")    # การแสดงผลข้อความ
print("1")

# comment

# Variable (ตัวแปร)
a = 5
b = 3
print(a)

print(a - b)

# input การรับค่า
n1 = input()    # input() จะรับค่าเป็น string
n2 = input()
print(int(n1) - int(n2))

# รับ input หลายบรรทัด
a = input()
b = input()
c = input()
print(a, b, c)

# รับ input 1 บรรทัด แบบคั่นด้วยเว้นวรรค
a, b, c = [int(x) for x in input().split()]
print(a)
print(b)
print(c)

a = "1 2 3".split() # การแบ่ง string
print(a)    # list of string

# วิธีทำให้ print ไม่ขึ้นบรรทัดใหม่
print("Hello ", end = "")
print("World")


a = 5
b = 3
print(a)

print(a - b)

# input การรับค่า
n1 = input()    # input() จะรับค่าเป็น string
n2 = input()
print(int(n1) - int(n2))
