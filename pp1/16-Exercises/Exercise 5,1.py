count = 0
total = 0
average = 0

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
    average = total/count
print(total, count, average)