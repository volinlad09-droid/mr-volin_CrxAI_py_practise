# Comparision Operators

print("Comparision Operators")

x = 20
y = 20

print("01.  == Equal :" , x == y)
print("02. != Not Equal : " , x != y)
print("03. > Greater Than : " , x > y)
print("04. < Less Than : " , x < y)
print("05. <= Less/Equal : " , x <= y)
print("06. >= Greater/Equal : " ,  x >= y)


# Logical Operator

print("Logical Operator")

a = True
b = False
c = False

print("01. and Logical AND  : " , a and b)
print("02. or Logical OR : " , a or b)
print("03. not Logical NOT : " , not b)

print((10 > 12 or 20 <= 20) and (10 > 20 or 40 > 25))

# Bitwise Operator


a = 10
b = 5

print("& Bitwise AND : " , a & b)
print("| Bitwise OR : " , a | b)
print("^ Bitwise XOR : " , a ^ b)
print("~ Bitwise NOT : " , ~b)
print(" << Left Shift :" , a << 1)
print(">> Right Shift : " , a >> 1)

# Conditional / Ternary Operator

age = 15

result = 'ADULT' if age >= 18 else 'MINOR'

print(result)

# Operator Precedence

result = 10 + 7 * 2

print(result)

# Type Conversion

# id()

a = 20
b = 21

print(id(a))
print(id(b))


# Identity Operator


x = [1 , 2 , 3]
y = x
z = [1 , 2 , 3]

print(x is y)
print(x is z)
print(x is not z)

# membership operator

numbers = [1 ,  2 , 3 , 4 , 5]

print(20 in numbers)
print(2 in numbers)
print(20 not in numbers)















