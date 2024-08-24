A = "" # empty string (string เปล่า) size = 0

# index of string
B = "Thailand 2024"
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# T h a i l a n d   2 0  2  4

# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  T   h   a   i   l  a  n  d     2  0  2  4

# call for value
print(B[12]) # "4"
print(B[-5]) # " "

# call for substring
print(B[2: 7]) # "ailan"
print(B[-10: 12]) # "iland 202"
print(B[2: -8]) # "ail"
print(B[5:]) # "and 2024"
print(B[-3:]) # "024"
print(B[: 10]) # "Thailand 2"
print(B[-6:]) # "d 2024"

# ----------------------------------------------------------------------------------

# + and * of string

# + of string (concatenate)
A = "COM"
B = "PUTER"
C = A + B
print(type(C))

# * of string
# string * int
A = "IkQ"
print(A * 3) # A * 3 = A + A + A
# if int is 0 or negative, the answer will be empty string
print(A * -2)

# ----------------------------------------------------------------------------------

# size and loop for string

# to find size of string we use len(name_string)
A = "F"
B = len(A)
print(B)

# loop
A = "25630"

print(A[0]) # "2"
print(A[1]) # "5"
print(A[2]) # "6"
print(A[3]) # "3"
print(A[4]) # "0"

for i in range(len(A)): # i = 0, 1, 2, 3, 4
    print(A[i])

