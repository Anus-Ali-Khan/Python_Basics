# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:      > 
# Less Than:         <
# Gretaer or Equal:  >=
# Less or Equal:     <=
# Object Identity    is (used to check if the values have same id or whether they are same object in memory)

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')


# and
# or
# not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Welcome')

# is operator
a = [1, 2, 3]
b = [1, 2, 3]
print(a==b) # this is true
print(a is b) # False beacause they are different objects and have different ids "is" operator check their ids in memory

print(id(a))
print(id(b))


# False Values
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = {} # put above values one by one

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')