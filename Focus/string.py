A = "" # string เปล่า มีขนาด คือ 0

# การบวก และการคูณของ string
B = "Thai"
C = "land"
D = B + C
# print(D, type(D))

# string คูณได้แค่กับ int
E = C * 5 # E = C + C + C + C + C
print(E)

# -----------------------------------------------------------------------------------------

A = "POSN-COMPUTER"
# ชื่อตำแหน่งใน string จะแทนด้วยตัวเลข
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# P O S N - C O M P U T  E  R

# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  P   O   S   N   -  C  O  M  P  U  T  E  R

# call for value
B = A[0] # "P"
C = A[-6] # "M"

# call for substring
# string_name[1st: 2nd] # ตำแหน่งแรกเอามาเลย แต่ตำแหน่งที่ 2 อย่าลืม +1
D = A[7: 11] # MPUT
E = A[-10: 8] # N-COM
# ตำแหน่งที่ 2 ว่าง คือเอาจนจบ
F = A[2:] # SN-COMPUTER
# ตำแหน่งแรกว่าง คือเอาตั้งแต่เริ่ม
G = A[: -5] # POSN-COM

# -----------------------------------------------------------------------------------------

A = "COWPUTER"
# A[2] = "M" แก้ string ตรงๆแบบนี้ไม่ได้

# การแก้ string ที่ถูกต้อง
B = A[0: 2] + "M" + A[3:]
print(B)

# -----------------------------------------------------------------------------------------

# การหาขนาด string และการวน string
A = "~Thailand! 2024."

# len(string_name) คืนค่าจำนวนตัวอังษรทั้งหมดเป็น int
length = len(A) # 16

for i in range(length): # 15
    print(A[i])
# ~
# T
# h
# a
# i
# l
# a
# n
# d
# !
#  
# 2
# 0
# 2
# 4
# .




