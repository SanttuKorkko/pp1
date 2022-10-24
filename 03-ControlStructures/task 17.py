x = int(input("Enter the first point (x): "))
y = int(input("Enter the second point (y): "))

point = (x,y)
if x > 0 and y > 0:
    print('Point P{} is in the first quadrant of the coordinate system'.format(point))
elif x < 0 and y > 0:
    print('Point P{} is in the second quadrant of the coordinate system'.format(point))
elif x < 0 and y < 0:
    print('Point P{} is in the third quadrant of the coordinate system'.format(point))
elif x > 0 and y < 0:
    print('Point P{} is in the fourth quadrant of the coordinate system'.format(point))
elif x == 0 and y == 0:
    print('Point P{} is in the middle of the coordinate system'.format(point))
else:
    print('Point P{} is between the quadrants'.format(point))    