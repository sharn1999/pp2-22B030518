import time

# list1 = [3,"f"]
# def mult(arr):
#     mul = 1
#     for i in arr:
#         mul = mul*int(i)
#     print(mul)
# for i in list1 :
#     if not str(i).isdigit():
#         raise ValueError("No str")
# mult(list1)


# string = "FSlkd*"

# def up(string):
#     countUpper = 0
#     countLower = 0
#     for i in string:
#         if i.isupper():
#             countUpper += 1
#         elif i.islower():
#             countLower += 1
#     print(countUpper)
#     print(countLower)
# if(isinstance(string, str)):
#     for i in string:
#         if i.isdigit():
#             raise ValueError("No str")
# else:
#     raise ValueError("No str")
# up(string)




# string = "abccba"

# def palindrom(string):
#     reversedStr= string[::-1]
#     if string == reversedStr:
#         print(f'{string} is a palindrome')
#     else:
#         print(f'{string} is not a palindrome')

# if(isinstance(string, str)):
#     for i in string:
#         if i.isdigit():
#             raise ValueError("No str")
# else:
#     raise ValueError("No str")

# palindrom(string)


# num = input()
# milli = input()
# try:
#     num = int(num)
#     milli = int(milli)
#     time.sleep(milli/1000)
#     print(f'Square root of {num} after {milli} miliseconds is {pow(num, 0.5)}')
# except ValueError:
#     raise ValueError('Not int')



# my_tuple = (1,7,5,20)

# if all(my_tuple):
#     print("All elements are true")
# else:
#     print("Not all elements tuple are true")