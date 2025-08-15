# Dictonaries: key - value pair
# key can be a string or integer
# student = {1:'John', 'age':25, 'courses':['Math','CompSci']}
student = {'name':'John', 'age':25, 'courses':['Math','CompSci']}

print(student)
print(student['name']) # if key doesm't exist in dict it will return error

# get(): method used to get value of specified key if it doesn't exist then iot will return None
print(student.get('phone')) # this will return None
# print(student.get('phone','Not Found'))

# add and update the dict
student['phone'] = '555-55555' # for single value

# update():method used to add and update the values in dict at once
student.update({'name': 'Jane', 'age': 26, 'phone': '555-55555' })
print(student)

# del : used to delete the key-value from dict
# del student['age']
age = student.pop('age')
print(student)
print(age)

# len: length of dict
print(len(student))

# keys
print(student.keys())

# values
print(student.values())

# both keys & values
print(student.items())

# loop throught dict
for key in student:
    print(key) # only print key

for key, values in student.items():
    print(key,values)