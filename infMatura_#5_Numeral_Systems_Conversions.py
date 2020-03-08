# From DECIMAL to BINARY using a built-in function
b = bin(123)
print(b[2:])

# From DECIMAL to BINARY using a list
print("\n")
def dectobin(number):
    arr = []
    while number >= 1:
        arr.append(number % 2)
        number //= 2
    return arr
result = dectobin(40)
result.reverse()
print(result)
# OR
# for i in range(len(result)-1, -1, -1):
#     print(result[i])

# From DECIMAL to BINARY using recursion and printing
print("\n")
def dectobin2(num):
    if num > 1:
        dectobin2(num // 2)
    print(num % 2, end=' ')

dectobin2(123)

# From DECIMAL to OCTAL using a built-in function
print("\n")
o = oct(123)
print(o[2:])

# From DECIMAL to OCTAL using recursion and printing
print("\n")
def dectoctal(num):
    if num > 1:
        dectoctal(num // 8)
    print(num % 8, end=' ')

dectoctal(123)