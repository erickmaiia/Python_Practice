import pandas as pd

# Exercise 1 - Create a structure that asks the user for the day of the week. if the day is
# equal to Sunday or equal to Saturday, print on the screen "Today is a day of rest", otherwise
# print on screen "You need to work!"

day = input('Enter the day of the week:')
if day == 'Sunday' or day == 'Saturday':
    print("Today is resting day")
else:
    print("You need to work!")

# Exercise 2 - Create a list of 5 fruits and check if the 'Strawberry' fruit is part of the list

list1 = ['Orange', 'Apple', 'Pineapple', 'Grape', 'Strawberry']
for fruit in list1:
    if fruit == 'Strawberry':
        print("Strawberry is part of the fruit list")

# Exercise 3 - Create a 4-element tuple, multiply each element of the tuple by 2 and save
# the results in a list

tuple1 = (1, 2, 3, 4)
list2 = []

for i in tuple1:
    list2.append(i * 2)
print(list2)

# Exercise 4 - Create a sequence of even numbers between 100 and 150 and print it on the screen

for i in range(100, 151, 2):
    print(i)

# Exercise 5 - Create a variable called temperature and assign the value 40. While temperature
# is greater than 35, print the temperatures on the screen

temperature = 40
while temperature > 35:
    print(temperature)
    temperature = temperature - 1

# Exercise 6 - Create a variable called counter = 0. As long as counter is less than 100,
# print the values on the screen, but when the value 23 is found, stop the execution of the
# program

cont = 0

while cont < 100:
    cont += 1
    print(cont)
    if cont == 23:
        print('program interrupted')
        break

# Exercise 7 - Create an empty list and a variable with value 4. While the variable's value
# is less than or equal to 20, add only even values to the list and print the list

list3 = []
x = 4

while x <= 20:
    x += 2
    list3.append(x)
print(list3)

# Exercise 8 - Transform the result of this range function into a list: range(5, 45, 2)
# nums = range(5, 45, 2)

nums = range(5, 45, 2)
print(list(nums))

# Exercise 9 - Correct the errors in the code below and run the program. Tip:
# are 3 errors.

temperature = float(input("What's the temperature? "))

if temperature > 30:
    print('Wear light clothes.')
else:
    print('Find your coats.')

# Exercise 10 - Write a program that counts how many times the letter "r" appears in the sentence below.
# Use a placeholder in your print statement
# “It is better, much better, to be content with reality; if she's not as bright as the ones
# dreams, has at least the advantage of existing.” (Machado de Assis)

phrase = "It is better, far better, to be content with reality; if it is not so bright \
like dreams, has at least the advantage of existing."

count = 0
for character in phrase:
    if character == 'r':
        count += 1
print(f"The character r appears {count} times in the sentence.")

# Exercise 11 - Create a function that prints the sequence of even numbers between 1 and 20
# (the function does not receive a parameter) and then make a call to the function to list
# the numbers


def func1():
    for i in range(2, 21, 2):
        print(i)


func1()

# Exercise 12 - Create a function that takes a string as an argument and returns the same
# string in capital letters. # Make a call to the function, passing a string as a parameter


def func2(string):
    return string.upper()


func2("hellow word!!")

# Exercise 13 - Create a function that takes as a parameter a list of 4 elements, adds 2
# elements to the list and print the list

list4 = [1, 2, 3, 4]


def func3(liist):
    liist.append(5)
    liist.append(6)


print(list4)
func3(list4)
print(list4)


# Exercise 14 - Create a function that takes a formal argument and a possible list of elements.
# make two calls to the function, with only 1 element and in the second call with 4 elements

def func4(arg, *list5):
    print(arg)
    for i in list5:
        print(i)
    return


func4(100)
func4('A', 'B', 'C')

# Exercise 15 - Create an anonymous function and assign its return to a variable called sum.
# The expression will receive 2 numbers as a parameter and return their sum


def suum(x, y): return x + y


suum(1, 2)

# Exercise 16 - Run the code below and make sure you understand the difference between global
# and local variable
total = 0


def suum2(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function: ", total)
    return total


suum2(10, 20)
print("Out of function: ", total)

# Exercise 17 - Below you will find a list with temperatures in degrees Celsius
# Create an anonymous function that converts each temperature to Fahrenheit
# Tip: to be able to perform this exercise, you must create your lambda function, inside
# a function (which will be studied in the next chapter).
# This allows you to apply your function to each element in the list How to find the math
# formula that converts from Celsius to Fahrenheit? Search!!!

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(list(Fahrenheit))

# Exercise 8
# Create a dictionary and list all dictionary methods and attributes

dic = {'key1': 'value1', 'key2': 'value2'}
dir(dic)

# Exercise 9
# Below you can find the Pandas import, one of the main Python packages for data analysis.
# Carefully review all available methods. One of them you will use in the next exercise.
dir(pd)

# Exercise 10 - Create a function that takes the file below as an argument and returns a descriptive statistical summary
# of the file. Tip, use Pandas and one of its methods, describe()
# File: "binary.csv"
# Set file location

file_name = "binary.csv"


def func5(file):
    df = pd.read_csv(file)
    return df.describe()


func5(file_name)
