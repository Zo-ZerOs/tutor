# DataType = ชนิดของข้อมูล

# int, float, string, bool
# Integer (int): จำนวนเต็ม 3, 5, -9, 0
# Float: จำนวนตรรกยะ (ทศนิยม) 3.1, -5.8, 0.0
# String: ข้อความ "Title" "1n9&^df4 sda! $sd"
# Boolean (bool): ค่าความจริง True, False

# int(DATA), float(DATA), str(DATA)

print(int(-3.9)) # remove decimal

print(float(2)) # add .0

# type() function: find type of data
print(type(2))

# ------------------------------------------------------------------------------------------

S = "Thailand"

# length, len(<str>): a number of letter in the string
print(len(S))
print(len("N'Tit   #@.18*/6le"))

# S = "Thailand"
# index similar to list
# index: 0 1 2 3 4 5 6 7
# data:  T h a i l a n d

# index: -8 -7 -6 -5 -4 -3 -2 -1
# data:   T  h  a  i  l  a  n  d

# access to a single letter
print(S[5]) # "a"
print(S[-7]) # "h"

# access to a substring
print(S[4: -2]) # "la"
print(S[-2: 3]) # edge-case -> ""
print(S[-7: -2]) # "haila"
print(S[3:]) # "iland"
print(S[: -5]) # "Tha"
print(S[:]) # "Thailand"
print(S[1: 1]) # ""




