A = "" # string เปล่ามีขนาดคือ 0

n = "Hello World"
# 0 1 2 3 4 5 6 7 8 9 10
# H e l l 0 _ W o r l d
print(n[6]) # เรียกดู string ตำแหน่งที่ 6

# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  H   e   l  l  0  _  W  o  r  l  d
print(n[-1]) # เรียกดู string ตำแหน่งที่ -1

print(n[3:7]) # เรียกดู string ตำแหน่งที่ 3 จนถึง 6


# ให้น้องปริ้น string ตำแหน่งที่ 4 และ 3 จากสุดท้าย
m = "aweasxdy"
print(m[-4:-2])

A = "ghfie mvkde"
# print(A[-10: 5])
# print(A[: 7]) # เรียกดูตำแหน่งแรกสุดจนถึงก่อนเลข 7
# print(A[4:]) # เรียกดูตำแหน่งที่ 4 จนถึงสุดท้าย

# -------------------------------------------------------------------------------------------------

# การบวก และการคูณ ของ string

# การบวก คือการเอา string มาต่อกันจะได้ string ใหม่
A = "abc"
B = "def"
print(A + B) # "abcdef"
print(B + A + B) # "defabcdef"
C = A[1:] + B[-2: 3] + B[: 1] # "bcefd"
print(C[: 2])

A = "Thailend2024"
# A[5] = "a" ไม่สามารถแก้ตัวอักษรใน string ด้วยวิธีนี้ได้
A = A[: 5] + "a" + A[6:] # วิธีการแก้ string ที่ถูกต้อง
print(A)

B = "POSN-COWPUTER" # 7 wrong
B = B[: 7] + "M" + B[8:]
print(B)

C = "SciEnCe ComPuter"
C = C[0] + "CI" + C[3] + "N" + C[5] + "E" + C[7: 9] + "OM" + C[11] + "UTER"
print(C)

# การคูณ string กับจำนวนเต็ม คือการต่อ string ซ้ำๆ
A = "abc" * 1 # A = "abc" + "abc" + "abc"
# ถ้าจำนวนเต็มเป็น 0 หรือติดลบ ผลลัพธ์จะได้ string เปล่า
print(A)

B = "df" * 5
print(B)

# -------------------------------------------------------------------------------------------------

# การหาขนาด และการวน

# การหาขนาด เราจะใช้ len(string_name)
X = "Rayong"
length = len(X) # int 6
print(length)

Y = "ThailandPOSN" # 0 1 2 ... 11
length = len(Y) # 12

for i in range(length):
    print(Y[i])
