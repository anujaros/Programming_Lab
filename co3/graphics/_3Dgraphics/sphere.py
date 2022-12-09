import graphics as gp
from graphics._3Dgraphics import *
a= gp.circle_area(10) ; p = gp.circle_perimeter(10)

print("Calling from graphics package:\nArea of circle:",a)
print("Perimeter of circle:",p)

print("Area of rectangle:",gp.r_area(5,10))
print("Perimeter of rectangle:",gp.r_area(5,10),"\n")


print("Calling from _3Dgraphics Subpackage:\nArea of SPhere:",surface_area(5))
print("Volume of sphere:",s_volume(5))

print("Area of cuboid:",total_s_area(4,8,10))
print("Volume of cuboid:",cuboid_volume(4,8,10))
