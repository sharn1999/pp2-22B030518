import math

deg = float(input("Input degree: "))

print(f'Output radian: {deg/57.2958}')

#///////////////////////

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

Area = (a+b)/2 * h

print(f"Expected Output: {Area}")

#/////////////////////////

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

area = s**2*(math.cos(math.pi/n)/math.sin(math.pi/n)) * n/4
print(f"The area of the polygon is: {area}")

#//////////////////////////

l = float(input("Length of base: "))
hp = float(input("Height of parallelogram: "))

print(f'Expected Output: {l*hp}')