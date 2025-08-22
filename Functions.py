#  "def" is used to create a function in python
def hello_func():
    print('Hello Function!')
    # pass
# pass: used to indicate that function doesn't return any value so python will not give any error

hello_func()

#  function allow us to do repetitive task easily

def hello_func2(greeting, name='You'): # we can also pass a default value in arguments of functions
    return '{}, {}'.format(greeting,name)

print(hello_func2('Hi', name = 'Corey'))

def student_info(*args,**kwargs): # *args denote tuple and **kwargs denote dictionary 
    print(args)
    print(kwargs)

# * and ** denotes the unpacked value of tuples and dict

courses = ['Math','Art']
info={'name':'John', 'age':32}

# print(student_info(courses,info)) # this will add both va;lues in tuple and print an empty dict becuse our function has * and ** so it receives unpacked values

# correct format
print(student_info(*courses,**info))

# print(student_info('Math', 'Art',name='John', age=22))
