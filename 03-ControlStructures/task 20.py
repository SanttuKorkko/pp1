x = 1
number = int(input('Enter any number: '))
while x >= 1 and x <= 10:
    print('{} x {} ='.format(number,x), int(number*x))
    x = x + 1
