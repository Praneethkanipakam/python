# DATA TYPES IN PYTHON 

'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

'''
# Arithmetic operators

#addition
a=100
b=200
print(a+b)

#Substraction
a=100
b=200
print(a-b)

#Multiplication
a=100
b=200
print(a*b)

#division
a=100
b=200
print(a/b)

#Modulus
#(the modulo gives reminder in division as a output)
a=100
b=200
print(a%b)

#Exponentiation
a=100
b=200
print(a**b)

# Floor division
a=100
b=200
print(a//b)

#Assignment operators

# The assignment operator in programming is used to assign values to variables. The most common assignment operator is the equals sign (=). For example:

# += (Addition assignment):       x += 5 is equivalent to x = x + 5
a=5
a += 3
print(a)

# -= (Subtraction assignment):    x -= 5 is equivalent to x = x - 5
a = 5
a -= 3
print(a)

# *= (Multiplication assignment): x *= 5 is equivalent to x = x * 5
a = 5
a *= 3
print(a)

# /= (Division assignment):       x /= 5 is equivalent to x = x / 5
a = 5
a /= 3
print(a) 

# %= (Modulus assignment):        x %= 5 is equivalent to x = x % 5
a = 5
a %= 3
print(a)

# **=(Exponentiation assignment): x **= 5 is equivalent to x = x ** 5
a = 5
a **= 3
print(a)

#(//=)(Floor division assignment): x //= 5 is equivalent to x = x // 5
a = 5
a //= 3
print(a)


# Comparision operators

# Equal to (==):
# Not equal to (!=): 
# Greater than (>):
# Less than (<):
# Greater than or equal to (>=):
# Less than or equal to (<=):

a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Logical operators:

# And - Returns True if both statements are true
# or  - Returns True if one of the statements is true
# not - Reverse the result, returns False if the result is true

a = 5
x = 5
print(x > 3 and x < 10)

a = 5
print(a > 3 or a < 4)

a = 5
print(not(a > 3 and a < 10))








