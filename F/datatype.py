# datatype - int (integer), float (rational number), string (text), Boolean (Truth value)

# int -> 3, 11, 45, 0, -8, -647
# whole number no decimal

# float -> 2.0, 3.78, -0.0, -85.2695
# with decimal

# string (str) -> "Hello", "123", "4f7g-869.hb2"
# with ""

# Boolean -> True, False

# type checking for both data and variable
print(type(3))
a = 5
print(type(a))

b = input() # <- 3 will be recieved as "3"
print(type(b))

#------------------------------------------------------------------------------------------------------------

# convert datatype

# converting string -> int can be done only if string contain only digit, 1 of "-"
# converting string -> float can be done only if string contain only digit, 1 of "-", 1 of "."
c = "23.2"
print(c, type(c))
c = int(c)
print(c, type(c))

d = int(input())
print(type(d))










