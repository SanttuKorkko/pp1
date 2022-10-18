from random import randrange
computer = randrange(1,7)
human = int(input("Try to guess computers roll: "))
if computer == human:
    print(True)
else:
    print(False)
