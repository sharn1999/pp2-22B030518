cars = ["Ford", "Volvo", "BMW"]

print(cars)

#/////////////

x = cars[0]

print(x)

#/////////////

cars[0] = "Toyota"

print(cars)

#////////////

y = len(cars)

print(y)

#////////

for x in cars:
  print(x)

#//////////

cars.append("Honda")
print(cars)

#/////////

cars.pop(3)

print(cars)

#/////////

cars.remove("Volvo")

print(cars)
