# while loop

# while condition:
#     statement

# condition == True => statement => condition == True => statement => ... => condition == False (end)

# while 1 == 1:
#     print("4")
# infinite loop

x = 5 # initial

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

# for x in range(y1, y2): # range(y1, y2) = [y1, y1 + 1, y1 + 2, ..., y2 - 1]
#     statement
# increasing by 1
# edge-case: y2 <= y1

# for x in range(y1, y2, y3): # range(y1, y2, y3) = [y1, y1 + y3, y1 + 2 * y3, ..., before y2]
#     statement
# edge-case: y1 == y2, (y1 < y2) and (y3 < 0), (y1 > y2) and (y3 > 0)
# y3 == 0 => True: error!!! bug!!!

for i in range(-4, 10, 2):
    print(i)

for i in range(99, -50, -17):
    print(i)

