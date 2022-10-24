quantity = 0
sum = 0
mean = 0
total = 0

while True:
    number = input('Enter number: ')
    if number == '0':
        break
    try:
        number = int(number)
    except:
        print('Not a number...')
        continue
    quantity = quantity + 1
    total = total + number
    sum += number
    mean = total/quantity
print('RESULT: Quantity={}, Sum={}, Mean={}'.format(quantity, sum, mean))