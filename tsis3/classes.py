class Smth:
    def __init__(self):
        self.inp = input()
    def printString(self):
        print((self.inp).upper())


Smth().printString()


class Square():
    def __init__(self, length = 0, width = 1):
        self.length = length
        self.width = width
        if(width == 1):
            self.area = length * length
        else:
            self.area = length * width
class Shape(Square):
    def Area(self):
        print(self.area)
Shape().Area()
Shape(5,8).Area()
Shape(2).Area()



class Point():
    def __init__(self, x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def show(self):
        print('x1: {}; x2: {}; y1: {}; y2: {}'.format(self.x1, self.x2, self.y1, self.y2))

    def move(self, x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def dist(self):
        distance = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print(distance)
point = Point(4,6,7,8)
point.show()
point.dist()
point.move(3,7,3,1)
point.show()
point.dist()

class Account():
    owner = "Olzhas"
    balance = 900
    def deposit(self, money):
        Account.balance += money
    def withdraw(self, money):
        if(money > Account.balance):
            print("Error, insufficient funds!!!")
        else:
            Account.balance -= money
Account().deposit(300)
print("Your balance: " + str(Account.balance))
Account().withdraw(3220)
print("Your balance: " +  str(Account.balance))
Account().withdraw(420)
print("Your balance: " +  str(Account.balance))

list1 = []
for x in range(3):
    list1.append(int(input()))

def delete(listx): 
    y = 2
    while y < listx**0.5:
        if(listx/y == round(listx/y)):
            return True
        y+= 1
    return False
out_filter = filter(delete, list1)
print(list(out_filter))
