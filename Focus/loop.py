# while loop การทำซ้ำ

# while condition:
#     statement

# check condition -> if True -> statment -> check condition -> if True -> statement -> ...

while True: # infinity loop
    print(1)

# บวกเลขตั้งแต่ 1 2 3 ... n
n = int(input())
sum = 0

while n != 0:
    sum = sum + n
    n = n - 1

print(sum)

# -----------------------------------------------------------------------------------------------------------

# for loop: เราสามารถกำหนดจำนวนครั้งตามค่า n ได้

# ปริ้น n ตัว
# for i in range(n):
#    statement

for i in range(10):
    print(i, end = " ") # ปริ้น 0 1 2 ... n-2 n-1

# ปริ้น n - a ครั้ง
# for i in range(a, n):
#    statement

for i in range(2, 5):
    print(i, end = " ") # ปริ้น a a+1 a+2 ... n-2 n-1

# (n - a) / x ปัดเศษขึ้น
# for i in range(a, n, x):
#     statement

for i in range(10, 25, 3):
    print(i, end = " ")




