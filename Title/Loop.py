# while loop

# while condition:
#     statement

# condition == True => statement => condition == True => statement => ... => condition == False (end)

# while 1 == 1:
#     print("4")
# infinite loop

x = 5 # initial

# statement ของ while จะอยู่หลังจาก while 1 tab
while x > 1: # condition
    print(x)
    x = x - 1 # update

# ------------------------------------------------------------------------------------------

# for loop

# for x in range(y): # range(y) = [0, 1, 2, ..., y - 1]
#     statement
# where x is str and y is int
# For iteration ith, x be will equal to ith element in the set
# edge-case: y <= 0
for i in range(5): # [0, 1, 2, 3, 4]
    print(i)

# for x in range(y1, y2): # range(y1, y2) = [y1, y1 + 1, y1 + 2, ..., y2 - 1]
#     statement
# increasing by 1
# edge-case: y2 <= y1
for i in range(-5, 2): # [-5, -4, -3, -2, -1, 0, 1]
    print(i)

# for x in range(y1, y2, y3): # range(y1, y2, y3) = [y1, y1 + y3, y1 + 2 * y3, ..., before y2]
#     statement
# edge-case: y1 == y2, (y1 < y2) and (y3 < 0), (y1 > y2) and (y3 > 0)
# y3 == 0 => True: error!!! bug!!!
for i in range(-14, 7, 2): # [-14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6]
    print(i)

# ------------------------------------------------------------------------------------------

# Flow Controling

# break: force to end the latest loop
x = 10
while True:
    x = x * 2
    if x > 500000:
        break

print(x)

# continue: skip current iteration to the next one
for i in range(50): # [0, 1, 2, ..., 49]
    if i % 7 == 0:
        continue
    print(i, end = " ")

