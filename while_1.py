
num = int(input('Please insert num: '))
den = int(input('Please insert den: '))
while den == 0:
    den = int(input('Please insert den: '))
    # from here jump to while condition

# from here means the while condition was false
print(num / den)
