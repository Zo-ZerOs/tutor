# for if, statement1 will be execueted if condition1 is True
# for elif, statement1 will be execueted if (the condition chain have never been True and condition of elif is "True")
# for else, statement4 will be executed if the condition chain have never been True

# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statemenet3
# else:
#     statement4

input = 0

if input == 1:
    print(1)
elif input > 3:
    print(3)
if input < 10:
    print(10)
elif input > 5:
    print(5)
else:
    print("No")

# ------------------------------------------------------------------------------------------------

# Boolean operator (== != > < >= <=)

# assign Truth value to a
a = True

# == 
# a == b, will be True if both sides of == is equal
print(5 == 5)
print(6 == 7)

# !=
# a != b, will be True if both sides of != is not equal
print(4 != 5)
print(1 != 1)

# >
# a > b will be True if a is more than b
print(7 > 5)
print(1 > 1)

# <
# a < b will be True if a is less than b
print(4 < 10)
print(3 < 1)

# >=
# a >= b will be True if a is more than or equal to b
print(3 >= -1)
print(4 >= 4)
print(1 >= 2)

# <=
# a <= b will be True if a is less than or equal to b
print(100 <= 1000)
print(30 <= 30)
print(20 <= 1.25)

# ------------------------------------------------------------------------------------------------

# Logic operator (not and or)

# not x will invert the truth value of x
print(not True)
print(not (7 < 4))

# and will be True if both sides are True
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(3 + 1 < 7 and 4 != 8)

# or will be False if both sides are False
print(True or True)
print(True or False)
print(False or True)
print(False or False)








