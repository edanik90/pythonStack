def sort_list(some_list):
    for i in range(len(some_list)):
        min = i
        for j in range(i,len(some_list)):
            if some_list[j] < some_list[min]:
                min = j
        if min != i:
            some_list[i], some_list[min] = some_list[min], some_list[i]
    return some_list
print(sort_list([6,2,10,15,4,7,21]))