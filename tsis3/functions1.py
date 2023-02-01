#1
def gramToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def toCelc(F):
    C = (5 / 9) * (F - 32)
    return C

#3
def solve(numheads, numlegs):
    rabbits = (numlegs - numheads*2)/2
    chickens = numheads-rabbits
    print('rabbits: {}; chickens: {}'.format(rabbits, chickens))


#4
def filterPrime(listx): 
    list2 = []
    for x in range(len(listx)):
        y = 2
        count = 0
        while y < listx[x]:
            if(listx[x]/y == round(listx[x]/y)):
                count = 1
                break
            y+= 1
        if(count == 0):
            list2.append(listx[x])
    return list2



#5

def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):
        words = list(string)
   
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)


#6
def reverse(string):
    list1 = []
    for x in range(len(string.split())):
        words = string.split()
        list1.append(words[len(words)-x-1])
    return " ".join(list1)



#7
def has_33(nums):
    for x in range(len(nums)):
        if(nums[len(nums)-1-x] == 3 and nums[len(nums)-2-x] == 3):
            if (len(nums)-2-x < 0):
                return False
            return True

#8
def spy_game(nums):
    zeros = 0
    seven = 0
    list1 = []
    for x in range(len(nums)):
        if(nums[x] == 0):
            zeros += 1
            list1.append(0)
        elif(nums[x] == 7):
            seven += 1
            list1.append(7)
    if((zeros == 2 and seven == 1) and list1 == [0,0,7]):
        return True



#9
import math
def volume(Radius):
    return 4/3 * math.pi * Radius**3


#10
def copyList(list1):
    newList = []
    for x in list1:
        if x not in newList:
            newList.append(x)
    return newList


#11
def isPalindrome(s):
    if(s == s[::-1]):
        print("Palindrom!")
    else:
        print("Not palindrom!")


#12
def histogram(list1):
    for x in range(len(list1)):
        print("*" * int(list1[x]))


#13
import random
def game():
    name = input("Hello! What is your name?\n" )

    print("Well, {}, I am thinking of a number between 1 and 20.\nTake a guess.".format(name))
    number = random.randint(1, 20)
    inp = 21
    count = 0
    while(inp != number):
        count += 1
        inp = int(input())
        if(inp < number):
            print("Your guess is too low.")
        elif(inp > number):
            print("Your guess is too high.")
        elif(inp == number):
            print("Good job, {}! You guessed my number in {} guesses!".format(name, count))
            break
