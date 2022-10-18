count = 0
total = 0
largest = None
smallest = None

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Invalid input')
        continue
    
    total = total + number
    count = count + 1
    for itervar in [number]:
        if smallest is None or itervar < smallest:
            smallest = itervar
            
    for itervar in [number]:
        if largest is None or itervar > largest:
            largest = itervar
print(total, count, smallest, largest)