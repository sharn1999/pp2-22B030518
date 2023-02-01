movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def check():
    global inp, pos
    pos = -1
    inp = input("Write the name of film\n")
    for x in range(len(movies)):
        pos += 1
        if(movies[x]['name'].lower() == inp.lower()):
            return True
    print("Oops, I can't find this movie. Let's try again")
    check()

def score(pos):
    if(movies[pos]["imdb"] > 5.5):
        return True
    else:
        return False

def subset(pos):
    if(score(pos)):
        return movies[pos]
    
def checkCategory():
    listCategory = []
    inp = input("Write the category of film\n")
    for x in range(len(movies)):
        if(movies[x]['category'].lower() == inp.lower()):
            listCategory.append(movies[x]['name'])
    return listCategory

def averageName(list1):
    listAver = []
    sum = 0
    for x in range(len(list1)):
        for y in range(len(movies)):
            if(movies[y]['name'].lower() == list1[x].lower()):
                listAver.append(movies[y]['imdb'])
    for j in range(len(listAver)):
        sum = sum + float(listAver[j])
    return sum / len(listAver)

def averageCategory(list1):
    listAver = []
    sum = 0
    for x in range(len(list1)):
        for y in range(len(movies)):
            if(movies[y]['name'].lower() == list1[x].lower()):
                listAver.append(movies[y]['imdb'])
    for j in range(len(listAver)):
        sum = sum + float(listAver[j])
    return sum / len(listAver)


check()
print(score(pos))
print(subset(pos))
categoryList = checkCategory()
print(categoryList)
print(averageName(['hitman', 'dark knight', 'we two']))
print(averageCategory(categoryList))