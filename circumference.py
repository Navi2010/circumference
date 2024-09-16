import math

def circle_circum(radius):
    return 2*math.pi*radius

radius = float(input('enter radius of circle: '))

total = circle_circum(radius)

print("the circumference of the circle is about: {:.2f}".format(total))