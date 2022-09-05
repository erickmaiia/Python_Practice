from time import strftime, localtime
# Exercise 1 - Create a list of 3 elements and calculate the third power of each element.

list1 = [3, 4, 5]
pow = list(map(lambda x: x**3, list1))

print(pow)

# Exercise 2 - Rewrite the code below, using the map() function. The end result must be
# the same!

words = 'The Data Science Academy offers the best data analysis courses in Brazil'.split()
result = list(map(lambda w: [w.upper(), w.lower(), len(w)], words))
for i in result:
    print(i)

# Exercise 3 - Calculate the transposed matrix of the matrix below.
# If you don't know what a transposed matrix is, visit this link:
# https://pt.wikipedia.org/wiki/Matriz_transposta
# Transposed matrix is a fundamental concept in the construction of artificial neural networks,
# AI systems base.

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in matrix:
    print(i)

# Exercise 4 - Create two functions, one to square a number and one to
# elevate to the cube.
# Apply both functions to the list elements below.
# Note: both functions must be applied simultaneously.

list2 = [0, 1, 2, 3, 4]


def square(x):
    return list(map(lambda x: x**2, x))


def cube(x):
    return list(map(lambda x: x**3, x))


for i in range(1):
    print(square(list2))
    print(cube(list2))

# Exercise 5 - Below you will find two lists. Make each element of listA be
# raised to the corresponding element in listB.

listA = [2, 3, 4]
listB = [10, 11, 12]
print(list(map(pow, listA, listB)))

# Exercise 6 - Considering the range of values below, use the filter() function
# to return only negative values.

range(-5, 5)


def less_than_zero(x):
    if x < 0:
        return True
    else:
        return False


print(list(filter(less_than_zero, range(-5, 5))))

# Exercise 7 - Using the filter() function,
# find the values that are common to the two lists below.

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]

print(list(filter(lambda x: x in a, b)))

# Exercise 8 - Consider the code below. Get the same result using the time package.
# Don't know the time package? Search!
# print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

print(strftime("%d/%m/%Y %H:%M", localtime()))

# Exercise 9 - Consider the two dictionaries below.
# Create a third dictionary with the keys from dictionary 1 and the values from dictionary 2.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}


def exchangeValues(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp


dict3 = exchangeValues(dict1, dict2)
print(dict3)

# Exercise 10 - Consider the list below and return only those elements whose index is
# greater than 5.

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for index, value in enumerate(list):
    if index <= 5:
        continue
    else:
        print(value)
