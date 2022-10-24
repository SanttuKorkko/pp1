x = int(input("Enter the dog's age in human years: "))
if x <= 2:
    age = float(x*10.5)
    print("The dog's age in dog's years is {} years.".format(age))
else:
    age = int(2*10.5)+int((x-2)*4)
    print("The dog's age in dog's years is {} years.".format(age))