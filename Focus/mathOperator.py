# + - * / ** // % (Operator)
# ถ้าเป็น int กับ float คอมจะเปลี่ยนให้กลายเป็น float กับ float

# 1) + (บวก)
print(4 + 3.5)
# บวกตรงๆ

# 2) - (ลบ)
print(5 - 3.2)
# ลบตรงๆ

# 3) * (คูณ)
print(10 * 5.1)
# คูณตรงๆ

# 4) / (หาร)
print((-11) / 5)
# จะได้คำตอบเป็น float เสมอ

# 5) ** (ยกกำลัง)
print((-5)**(1/2))
# ถ้าหาsquare rootจำนวนติดลบ เราจะได้ imaginary number

# 6) // (หารปัดเศษ)
print((-3)//2)
# 6.1) หารแบบปกติก่อน
# 6.2) ปัดทศนิยมลง
# 6.3) ถ้ามี float คำตอบจะเป็น float

# 7) % (เศษจากการหาร) mod
print(-10 % 7)

# a, b
# a // b = x
# a % b = y
# a = b*x + y

# -10, 7
# (-10) // 7 = -2
# (-10) % 7 = y
# -10 = 7 * (-2) + y
# -10 = -14 + y
