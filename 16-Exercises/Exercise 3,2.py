hours=input('Enter Hours: ')
try:
    int(hours)
    rate=input('Enter Rate: ')
    int(rate)
    pay = int(hours) * int(rate)
    int(pay)
    print(pay)
except:
    print('Error, enter numeric input')