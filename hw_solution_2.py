#input a number. check if the number is 0 or 1, if so print ‘0 or 1’
#otherwise check if the number is -1, if so print ‘-1’
#otherwise print ‘unknown number’

number = int(input('Please enter a number: '))
if number == 0 or number == 1:
    print('0 or 1')
else:
    if number == -1:
        print('-1')
    else:
        print('unknown number')
