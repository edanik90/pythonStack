# 1 Biggie Size
def biggie_size(my_list):
    for i in range(0,len(my_list)):
        if my_list[i] > 0:
            my_list[i] = 'biggie'
    return my_list
print(biggie_size([-3, 2, 6, -2, 4, -10, 20]))

# 2 Count Positives
def count_positives(my_list):
    num = 0
    for i in my_list:
        if i > 0:
            num = num + 1
    my_list[len(my_list) - 1] = num
    return my_list
print(count_positives([-1, 2, 4, -1, 2, -2, 5]))

# 3 Sum Total
def sum_total(my_list):
    sum_values = 0
    for i in my_list:
        sum_values = sum_values + i
    return sum_values
print(sum_total([1,3,5,2]))

# 4 Average
def average_of_values(my_list):
    sum_values = 0
    for i in my_list:
        sum_values = sum_values + i
    return sum_values / len(my_list)
print(average_of_values([2,4,5,3]))

# 5 Length
def length_of_list(my_list):
    return len(my_list)
print(length_of_list([2,2,-1,-2,6,10]))

# 6 Minimum
def minimum_value(my_list):
    if len(my_list) == 0:
        return False
    min_value = my_list[0]
    for i in my_list:
        if i < min_value:
            min_value = i
    return min_value
print(minimum_value([0,1,5,20,-1,2,-4]))

# 7 Maximum
def maximum_value(my_list):
    if len(my_list) == 0:
        return False
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value
print(maximum_value([0,1,5,20,-1,2,21,3]))

# 8 Ultimate Analysis
def ultimate_analysis(my_list):
    my_dict = {}
    my_dict['sumTotal'] = sum_total(my_list)
    my_dict['Average'] = average_of_values(my_list)
    my_dict['Maximum'] = maximum_value(my_list)
    my_dict['Minimum'] = minimum_value(my_list)
    my_dict['Length'] = length_of_list(my_list)
    return my_dict
print(ultimate_analysis([2,-3,5,2]))

# 9 Reverse list
def reverse_list(my_list):
    for i in range(0,int(len(my_list)/2)):
        temp = my_list[i]
        my_list[i] = my_list[len(my_list)-i-1]
        my_list[len(my_list)-i-1] = temp
    return my_list
print(reverse_list([20,4,1,6,-8,2,-20]))
