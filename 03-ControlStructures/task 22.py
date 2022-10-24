x = 1
while x >= 1 and x <= 30:
    
    if x%3 == 0 and x%5 == 0:
        print('BINGO')
    elif x%5 == 0:
        print('FIVE')
    elif x%3 == 0:
        print('THREE')
    else:
        print(x)
    x = x + 1
    