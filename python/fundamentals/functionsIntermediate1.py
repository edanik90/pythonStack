import random
def randInt1(min = 0, max = 100):
    num = random.random()*max
    return round(num)
print(randInt1()) # should print a random integer between 0 to 100

def randInt2(max, min = 0):
    num = random.random()*max
    return round(num)
print(randInt2(max=50)) # should print a random integer between 0 to 50

def randInt3(min, max = 100):
    num = random.random()*50+50
    return round(num)
print(randInt3(min=50)) # should print a random integer between 50 to 100

def randInt4(min, max):
    num = random.random()*450+50
    return round(num)
print(randInt4(min=50, max=500)) # should print a random integer between 50 and 500
