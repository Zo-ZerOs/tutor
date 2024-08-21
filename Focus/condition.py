# if condition:
#   statement
# elif condition:
#   statement
# else:
#   statement

a = 5

if a < 3:
    print("less")
elif a == 3:
    print("333")
elif a > 4:
    print("444")
if a == 5:
    print("555")
elif a == 6:
    print("666")
else:
    print("more")

print("Hello")


# Boolean operator (< > == != <= >= and or in)

if 3 < 5:
    print("less")

if 5 > 2:
    print("more")

if 3 == 3:
    print("equal")

if 4 != 5:
    print("not equal")

if (2 < 3) and (4 == 4):
    print("and")

if (2 > 3) or (4 == 4):
    print("or")

if 2 <= 3:      # (2 < 3) or (2 == 3)
    print("less or equal")

if 4 >= 3:      # (2 > 3) or (2 == 3)
    print("more or equal")

if "a" in "abc":
    print("in")

# string comparation: "0" < "9" < "A" < "Z" < "a" < "z"
print("0" < "9")
print("a12fdg2" == "a12ppu") # เราจะเปรียบเทียบ string ที่ละตำแหน่งเริ่มจากซ้ายมือสุดไล่ไปขวาเลื่อยๆ

# if condition:
#     T = value1
# else:
#     T = value2

# T = value1 if condition else value2

T = 1 if 1 != 1 else 2
print(T)
