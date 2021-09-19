#input a number. check if the number is 0 or 1, if so print ‘0 or 1’
#otherwise check if the number is -1, if so print ‘-1’
#otherwise print ‘unknown number’

number = int(input('Please enter a number: '))
if number == 0 or number == 1:
    print('0 or 1')
#else
# if number == -1:
elif number == -1:
  print('-1')
else:
  print('unknown number')

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

