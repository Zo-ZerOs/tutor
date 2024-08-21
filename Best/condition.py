# ถ้า condition1 เป็นจริงให้ทำ statement1 
# แต่ถ้าไม่ต้องดู condition2 ถ้าเป็นจริงให้ทำ statement2
# แต่ถ้าไม่ต้องดู condition3 ถ้าเป็นจริงให้ทำ statement3
# นอกจากนั้นให้ทำ statement4
# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statement3
# else:
#     statement4

a = int(input())
b = 0
c = 0
d = 0

if a > 2:
    b = 1
    c = 2
    d = 3
else:
    b = a
    c = b
    d = d

print(b, c, d)




