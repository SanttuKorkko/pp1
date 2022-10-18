
a = int(input("Lenght of side a: "))
b = int(input("Lenght of side b: "))
c = int(input("Lenght of side c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
print(f"Are of the triangle is {area}.")