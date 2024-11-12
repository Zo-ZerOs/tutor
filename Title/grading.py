# input : int(score)

# output : print -> str(grade)
# score in [0, 49] => F
# score in [50, 59] => D
# score in [60, 69] => C
# score in [70, 79] => B
# score in [80, 100] => A
# score not in [0, 100] => error

# Example
# 5 -> F
# 76 -> B

# ------------------------------------------------------------------------------------------

score = int(input("Enter your score (0 - 100): "))

if 0 <= score <= 49:
    print("F")
elif 50 <= score <= 59:
    print("D")
elif 60 <= score <= 69:
    print("C")
elif 70 <= score <= 79:
    print("B")
elif 80 <= score <= 100:
    print("A")
else:
    print("error")

print("Finish")


