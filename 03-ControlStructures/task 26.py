correct = "0805"

def verify_pin(pin):
    if pin == correct:
        return True
    else:
        return False
    
tries = 0
    
while tries < 3:
    pin_code = input('Enter the PIN code: ')
    if verify_pin(pin_code):
        print('Correct')
        break
    else:
        print('Incorrect...')
    tries += 1
else:
    print('Sorry, your payment card has been blocked.')
        