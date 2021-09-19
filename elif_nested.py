# input a word from the user -- string
# translate the word into number,
# i.e. : 'one' print 1
# i.e. : 'two' print 2
# .. till 5
# otherwise print 'out of scope'
word_number = input('Please enter the text of a number: ')
x = int(input('Please enter x (number): '))
if word_number == 'one':
    print(1)
elif word_number == 'two':
    print(2)
    if x > 1:
        print('bigger than ')
    elif x == 0:
        print('zero')
    else:
        print('x smaller equal than 1')
elif word_number == 'three':
    print(3)
elif word_number == 'four':
    print(4)
elif word_number == 'five':
    print(5)
else:
    print('out of scope')

