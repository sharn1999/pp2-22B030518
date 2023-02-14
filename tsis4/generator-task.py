def gensquares(N):
    for i in range(N): 
        yield i**2

for x in gensquares(N=5):
    print(x)

#?/////////////////////////////

def even(N):
    for i in range(N): 
        if(i%2 == 0):
            yield i

list1 = []
for x in even(N=5):
    list1.append(x)

print(*list1, sep=', ')

#//////////////////

def div(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for x in div(100):
    print(x, end=" ")
print()

#///////////////////

def squares(a, b):
    for i in range(a, b+1):
        yield i*i
for x in squares(1, 10):
    print(x, end=' ')
print()
#///////////////////

def cn(n):
    while n >= 0:
        yield n
        n -= 1
for x in cn(10):
    print(x, end=' ')