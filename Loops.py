nums = [1, 2, 3, 4, 5]


# break : it breaks the loop when condition is met

for num in nums:
    if num == 3:
        print('Found!')  
        print('*******************')  
        break
    print(num)

# continue: it skips that iteration where condition is met  
for num in nums:
    if num == 3:
        print('Found!')    
        continue
    print(num)

# Nested Loops
for num in nums:
    for letter in 'abc':
        print(num,letter)

# range: run the loop for specific number of iteration
for i in range(1, 11):
    print(i)

# while Loop : run until certain condition is met
x = 0
while x < 10:
    if(x ==5 ):
        break
    print(x)
    x += 1 
    
