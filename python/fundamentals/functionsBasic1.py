# 1
def a():
    return 5
print(a())  # prints what was returned from function, which is 5

# 2
def a():
    return 5
print(a()+a())  # a() = 5, so a()+a() = 5 + 5 = 10

# 3
def a():
    return 5  # returns 5 and ends the function
    return 10  # will not run, because return statement was already used before
print(a())  # prints 5

# 4
def a():
    return 5  # returns 5 and ends the function
    print(10)  # will not run, because return statement was used in previous line
print(a())  # prints 5

# 5
def a():
    print(5) # prints 5
x = a()
print(x)  # prints None, since nothing has been returned from function a()

# 6
def a(b, c):
    print(b+c)
    # a(b,c) -> a(1,2) -> b = 1, c = 2 -> b+c -> 1+2=3
    # a(b,c) -> a(2,3) -> b = 2, c = 3 -> b+c -> 2+3=5
print(a(1, 2) + a(2, 3)) # gives an error, because nothing has been returned from fucntion a()

#7
def a(b,c):
    return str(b)+str(c) # str(b) and str(c) converts their values to a strings
print(a(2,5)) # prints bc -> 25 as a string

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5 # 100 isn't greater than, so this will not run
    else:
        return 10 # returns 10
    return 7
print(a()) # would print b, which is 100, and 10, which is a return from function

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # 2<3 is true, so returns and prints 7
print(a(5,3)) # 5<3 is false, so returns and prints 14
print(a(2,3) + a(5,3)) # a(2,3) -> 7.  a(5,3) -> 14.  7 + 14 = 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # b = 3, c = 5. Returns and prints b + c -> 3 + 5 = 8

#11
b = 500
print(b) # prints 500
def a():
    b = 300
    print(b)
print(b) # prints 500
a() # calls function a() and prints b, which is 300
print(b) # prints 500

#12
b = 500
print(b) # prints 500
def a():
    b = 300
    print(b)
    return b
print(b) # prints 500
a() # calls function a() and prints b, which is 300
print(b) # prints 500

#13
b = 500
print(b) # prints 500
def a():
    b = 300
    print(b)
    return b
print(b) # prints 500
b=a() # calls function, returns 300 from it, so now new value of b is 300 and prints 300
print(b) # prints 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # calls function a(), prints 1, calls function b(), which prints 3, then prints 2

#15
def a():
    print(1) #prints 1
    x = b() # calls b(), which prints 3, returns 5 from it, so now x = 5
    print(x) # prints 5
    return 10
def b():
    print(3)
    return 5
y = a() # calls a(), returns 10 from it, so now y = 10
print(y) # prints 10