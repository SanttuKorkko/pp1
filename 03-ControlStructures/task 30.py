num = int(input("Enter a number: "))
x = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            x = True
            break
if x:
    print("Not a prime number")
else:
    print("Prime number")