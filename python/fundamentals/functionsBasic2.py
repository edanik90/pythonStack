# 1 Countdown
def count_down(num):
    new_list = []
    for i in range(num,-1,-1):
        new_list.append(i)
    return new_list
print(count_down(9))

# 2 Print and Return
def print_return(list):
    print(list[0])
    return list[1]
x = print_return([5,9])
print(x)

# 3 First Plus Length
def first_plus_length(list):
    Sum = list[0] + len(list)
    return Sum
y = first_plus_length([8,4,3,1,4])
print(y)

# 4 Values Greater than Second
def values_greater_than_second(list):
    new_list = []
    num_of_values = 0
    if len(list) < 2:
        return False
    for i in list:
        if (i > list[1]):
            new_list.append(i)
            num_of_values = num_of_values + 1
    return num_of_values, new_list

z = values_greater_than_second([5,2,4,2,1,6])
print(z)

# 5 This Length, That Value
def length_and_value(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
b = length_and_value(4,13)
print(b)