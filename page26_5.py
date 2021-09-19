
sum = 0
x = int(input('please enter a non-negative number [-99 to exit]: '))

while x != -99:
    sum += x
    x = int(input('please enter a non-negative number [-99 to exit]: '))
    
print('sum=', sum)
