# input 2 numbers
a = int(input('Please enter number #1: '))
b = int(input('Please enter number #2: '))

# place the small number inside small 
#   and the bigger number in big 
if a > b:
    small = b
    big = a
else:    
    small = a
    big = b
    
# i indexer starts from small
i = small

# iterate from small to big and print
while i <= big:
    print(i)
    i += 1

