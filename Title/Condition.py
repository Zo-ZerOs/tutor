# condition: if-else

# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statement3
# elif condition4:
#     statement4
# ...
# elif condition(n-1):
#     statement(n-1)
# else:
#     statement

# condition1 == True => statement1
# condition1 == False => condition2 == True => statement2
# condition1 == False => condition2 == False => condition3 == True => statement3
# ...
# condition1 == False => condition2 == False => condition3 == False => condition4 == False => ... => condition(n-1) == False => statementn

y = int(input())

if y == 5:
    print("Equal to 5")
else:
    print("Hay")
    print("LoL")
    print("T-T")


