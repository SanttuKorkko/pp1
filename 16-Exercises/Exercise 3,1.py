hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours)*float(rate)
pay1 = 40*float(rate) + ((float(hours) - 40) * (float(rate) * 1.5))

if float(hours) > 40:
    print(pay1)
else:
    print(pay)