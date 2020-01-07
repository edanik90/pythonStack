# 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry', 'Leonard', 'Irving'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney', 'Mane', 'Firmino', 'Mbappe', 'Vardy', 'Kane']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]['last_name'] = 'Bryant'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)


# 2 Iterate Through a List of Dictionaries
def iterateDictionary(my_list):
    for item in my_list:
        print('first_name -', item['first_name'] + ', last_name -', item['last_name'])
iterateDictionary(students)


# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
iterateDictionary2('first_name', students)

# 4 Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{len(v)} {k}")
        for item in v:
            print(item)
printInfo(sports_directory)

