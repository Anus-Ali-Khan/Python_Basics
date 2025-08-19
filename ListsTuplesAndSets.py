#  Lists and Tuples allowed us to work with sequential data
#  Sets are unordered collection of values with no duplicates

# Lists:
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))

# Indexing
print(courses[1])

# Negative Indexing
print(courses[-1]) # It works from end of a list

# Slicing of List
print(courses[0:2]) # first is inclusive and last is exclusive
print(courses[:2]) # Starts from index 0
print(courses[2:])  # Ends at last index

# append: Add Item at last index of list
courses.append('Art')
print(courses)

# insert: add item at specified index
courses.insert(0,'Art')
print(courses)

# extend: if we have another list courses_2 and we want to add its item in courses so we use extend instead of insert beacuse insert will put whole list in first one.

courses_2=['Art','Education']
courses.extend(courses_2)
print(courses)

# remove : remove item from list
courses.remove('Math')

# pop: remove last item of list and return it
popped = courses.pop()
print(popped)

# reverse: reverse the list
# sort: sort the list in ascending order
nums=[1,5,2,4,3]
nums.sort()

# sort in descending order
nums.sort(reverse=True)
courses.sort(reverse=True)
print(courses)
print(nums)

# All these above methods alter the original list
# But if we don't want alter the original one so we use sorted() function
sorted_courses = sorted(courses)
print(sorted_courses,'sorted_courses')

# min, max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

# find index of value
print(courses.index('CompSci'))

# check value exist in list or not
print('Math' in courses)
print('Art' in courses)

# for loop and enumerate function (gives index and items in list)
for index,course in enumerate(courses, start=1):
    print(index,course)

# join: method use to convert list into string seperated by comma,hyphen etc
course_str = ', '.join(courses)
print(course_str)

# split: method convert string into list
new_list = course_str.split(', ')
print(new_list)
    
# Lists are mutubale(can be modified)
# Tuples : similar to list but they are immutable(cannot be modified)


# Mutuable Example
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

# Since its a list so both list will change
print(list_1)
print(list_2) 

# Immutable Example
# Tuples are created by using round bracket
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # it will throw error because tuple are immutable

# print(tuple_1)
# print(tuple_2)

# Sets: unordered values and have no duplicates
# if we add duplicate in it. It will automatically remove it
# curly braces are used

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# Sets do membership test more efficiently than tuples and lists
print('Math' in cs_courses)

# intersection: method use to check the same items in two sets 
print(cs_courses.intersection(art_courses))

# difference: method use to check the different courses in two sets
print(cs_courses.difference(art_courses))

# union: combine two sets
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list() #class method

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dictonary
empty_set = set() # this is perfect