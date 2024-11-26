# List is one of DataStructure

A = [] # Empty List
B = [1, 4, -4, 7] # initialize list of int
C = [1.2, -9.8, 4.0] # initialize list of float
D = ["", "x", "Title", "H3110 W0RLD"] # initialize list of string
E = [True, True, False] # initialize list of Boolean
F = [1, -9.5, "one", "15", True] # initialize multiple-type list
G = [1, [-8.7, "5t7-!"], [[[[True]]], "1", 1], 1] # initialize multiple-layer list

# ------------------------------------------------------------------------------------------

# length, len(<list>): a number of element in the list
print(len(B)) # 4
print(len(F)) # 5
print(len(G)) # 4

# we call each of the data inside list as "element"
X = [-2, -1, 0, 1, 2] # index's domain = from -5 to 4
# index: 0  1 2 3 4
# data: -2 -1 0 1 2

# index: -5 -4 -3 -2 -1
# data:  -2 -1  0  1  2

# the "index" of elements mostly start at 0, then increment by 1
# the "index" of elements mostly start at -length, then increment by 1

AA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# -N -N+(1) -N+(2) ... -N+(N-2) -N+(N-1)=-1
# The ith element from RHS will correspond to the index = -i

# T = [1, "f", True, 6, 0, -1.2, 8, ...]
# len(T) = N
# index's domain = from -N to N-1

# ------------------------------------------------------------------------------------------

# X = [-2, -1, 0, 1, 2]
# AA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# access a single element
print(X[2]) # access to index 2 of the list
print(X[-4]) # access to index -4 of the list
# print(X[10]) # edge-case -> error("list index out of range")
# print(X[-6]) # edge-case -> error("list index out of range")

# access a sublist
print(X[1: 3]) # [-1, 0]
print(AA[4: 8]) # [5, 6, 7, 8]
print(AA[-8: 10]) # [6, 7, 8, 9, 10]
print(AA[-2: 5]) # edge-case -> []
print(AA[3:]) # start from index 3 to the end -> [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(AA[: -5]) # start from index 0 to index -5 -> [1, 2, 3, 4, 5, 6, 7, 8]
print(AA[:]) # the entire list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(AA[7: 7]) # []

# ------------------------------------------------------------------------------------------

# concatenate list: เอา list มาต่อกันเฉย ๆ 
B = [2, 4, 6]
C = [4, 2, 9, 10]
D = B + C
print(D)

# append list: เพิ่ม element ไว้ตัวสุดท้ายของ list
# print(B.append(1))
print(B + [1])






