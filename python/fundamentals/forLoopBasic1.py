# 1 Basic
for i in range(151):
    print(i)

# 2 Multiples of Five
for i in range(5, 1001):
    print(i*5)

# 3 Counting, the Dojo Way
for i in range(1, 101):
    if(i % 10 == 0):
        print('Coding Dojo')
    elif(i % 5 == 0):
        print('Coding')
    else:
        print(i)

# 4 Whoa. That Sucker's Huge
finalSum = 0
for i in range(500001):
    if(i % 2 != 0):
        print(i)
        finalSum = finalSum + i
print(finalSum)

# 5 Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6 Flexible Counter
lowNum = 3
highNum = 24
mult = 8
for i in range(lowNum, highNum + 1):
    if(i % mult == 0):
        print(i)
