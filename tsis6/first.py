import os


path = "C:\work\python"

# print("Directories:")
# for name in os.listdir(path):
#     if os.path.isdir(os.path.join(path, name)):
#         print(name)

# print("\nFiles:")
# for name in os.listdir(path):
#     if os.path.isfile(os.path.join(path, name)):
#         print(name)

# print("\nAll Directories and Files:")
# for dirpath, dirnames, filenames in os.walk(path):
#     for name in dirnames + filenames:
#         print(os.path.join(dirpath, name))


# if os.path.exists(path):
#     print(f'{path} exists')
#     if os.access(path, os.R_OK):
#         print(f'{path} is readable')
#     else:
#         print(f'{path} is not readable')
#     if os.access(path, os.W_OK):
#         print(f'{path} is writable')
#     else:
#         print(f'{path} is not writable')
#     if os.access(path, os.X_OK):
#         print(f'{path} is executable')
#     else:
#         print(f'{path} is not executable')
# else:
#     print(f'{path} does not exist')


# if os.path.exists(path):
#     directory, filename = os.path.split(path)
#     print(f'Directory: {directory}')
#     print(f'Filename: {filename}')



# num = 0

# with open('text1.txt', 'r') as file:
#     for line in file:
#         num += 1

# print(num)


# list1 = ['aefdaw', 'awdaREFW', 'ESFEF']
# with open('text2.txt', 'w') as file:
#     for i in list1:
#         file.write(f'{i}\n')


# for i in range(65, 91):
#     open(f'{chr(i)}.txt', 'w+')


# txt1 = 'text3.txt'
# copy = 'text3-copy.txt'
 
# with open(txt1, 'r') as f:
#     data = f.read()
 
# with open(copy, 'w') as f:
#     f.write(data)

# path2 = f"C:\work\python\\tsis6\delete.txt"
# if os.path.exists(path2):
#     print(f'{path2} exists')
#     if not os.access(path2, os.R_OK):
#         print(f'Error! Not readable')
#         exit()
#     if not os.access(path2, os.W_OK):
#         print(f'Error! Not writable')
#         exit()
#     if not os.access(path2, os.X_OK):
#         print(f'Error! Not executable')
#         exit()
#     os.remove(path2)
#     print(f'{path2} has been deleted')