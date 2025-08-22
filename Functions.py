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


# Calculation of Leap Year

# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """Return number of days in that month in that year"""
    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017,2))

