# data structure

A = [] # empty list มีขนาด 0
B = [2, 5, 1, 4] # list of int
C = [1.5, -2.8, 0.0] # list of float
D = [5, -3.8, "Hello", False, -9, 0.16, "World", True] # list

# index of list
A = ["a", "b", "c", "d", "e", "f", "g"]
#  0   1   2   3   4   5   6
# "a" "b" "c" "d" "e" "f" "g"

# -7  -6  -5  -4  -3  -2  -1
# "a" "b" "c" "d" "e" "f" "g"

# call for value
print(A[2]) # "c"
print(A[-4]) # "d"

# call for sublist
print(A[1: -2]) # ["b", "c", "d", "e"]
print(A[-4:]) # ["d", "e", "f", "g"]
print(A[: 3]) # ["a", "b", "c"]

# ----------------------------------------------------------------------------------

# + and * of list

# + of list (concatenate)
A = [1, 2, 3]
B = [1, 4, 2]
print(A + B) # [1, 2, 3, 1, 4, 2]

# * of string
A = [1, 2, 3]
B = A * 3 # B = A * 3 = A + A + A
print(B)

# ----------------------------------------------------------------------------------

# size and loop for list

# to find size of list we use len(name_list)
A = [1, 2, 3]
B = len(A)
print(B)

# loop
A = ["a", "b", "c", "d", "e"]

for i in range(len(A)): # i = 0, 1, 2, 3, 4
    print(A[i])






