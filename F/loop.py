# while condition:
#     statement

# check condition -> True -> statement -> check condition -> True -> statement -> check condition -> False -> Break loop

a = 1 # initial

while a <= 100: # condition
    print(a)
    a += 1 # update

# when condition always True -> infinite loop

# ------------------------------------------------------------------------------------------------

# for i in range(parameter):
#     statement

# for x in range(n): # assign value to x from 0 to n - 1 increasing by 1
#     print(x, end = " ")

for i in range(5): # i = 0, 1, 2, 3, 4
    print(i)

# for x in range(a, n): # assign value to x from a to n - 1 increasing by 1
#     print(x)

for i in range(3, 8): # i = 3, 4, 5, 6, 7
    print(i)

# for x in range(a, n, s): # assign value to x from a to (n - 1 if s is positive) (n + 1 if s is negative) increasing by s
#     print(x)

for i in range(7, -2, -3): # i = 7, 4, 1
    print(i)

