amount = int(input('Enter the amount in PLN: '))
five = (amount//5)
print('5 PLN -',five)
two = (amount-five*5)//2
print('2 PLN -',two)
one = int((amount-five*5-two*2)//1)
print('1 PLN -',one)