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
print(print_return([5,9]))

# 3 First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([8,4,3,1,4]))

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
print(values_greater_than_second([5,2,4,2,1,6]))

# 5 This Length, That Value
def length_and_value(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(4,13))