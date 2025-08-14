my_message1 = 'Hello\'s World'
my_message2 = "Hello's World"
my_message3 = """Bobby's World was a good
cartoon in 1990's"""  
# In python multi name variables are seperated by under score
# Triple quotes are used to write multi lines of code
# len function is used to find length of string 
print(my_message3)
print(len(my_message1))

# address the location of single alphabet
print(my_message1[10])


# slicing a apart from string start index is inclusve but last index is exclusive
print(my_message1[0:5])

# It will start from begining builtin
print(my_message1[:5]) 

# It will go to end automatically
print(my_message1[6:]) 

print(my_message1.lower()) 
print(my_message1.upper())

# Count certain number of letters in string
print(my_message1.count('l')) 

# find: gives the index of specfic letter and for complete word it gives starting index
print(my_message1.find('World')) 
# the word that doesn't exist it returns -1
print(my_message1.find('universe')) 


# replace : replace the some characters with other
new_message = my_message1.replace('World','Universe')
print(new_message)


# concatenation
greeting =  'Hello'
name = 'Michael'

message1 = greeting + ' ' + name + '. Welcome!'
message2 = '{}, {}. Welcome!'.format(greeting,name)
message3 = f'{greeting}, {name.upper()}. Welcome!'

print(message3)

# dir: show methods that can be applied to this varaiable
print(dir(name)) 

# to see available methods with description
print(help(str.lower))