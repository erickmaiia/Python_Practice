# Exercise 1 - Print the numbers from 1 to 10 on the screen. Use a list to store the numbers.

list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)

# Exercise 2 - Create a list of 5 objects and print it on the screen

list2 = ['Erick', 19, 1.74, True, 'Books']
print(list2)

# Exercise 3 - Create two strings and concatenate the two into a third string

x = 'Hello '
y = 'Word!'
z = x + y
print(z)

# Exercise 4 - Create a tuple with the following elements: 1, 2, 2, 3, 4, 4, 4, 5 and then use the count function of
# tuple object to check how many times the number 4 appears in the tuple

tuple1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tuple1.count(4))

# Exercise 5 - Create an empty dictionary and print it to the screen

dict1 = {}
print(dict1)

# Exercise 6 - Create a dictionary with 3 keys and 3 values ​​and print it on the screen

dict2 = {
    'name': 'Erick',
    'age': 19,
    'height': 1.74,
}
print(dict2)

# Exercise 7 - Add one more element to the dictionary created in the previous exercise
# and print it on the screen

ditc3 = {'programer': True}
dict2.update(ditc3)
print(dict2)

# Exercise 8 - Create a dictionary with 3 keys and 3 values. One of the values ​​must be a list of 2 numeric
# elements. Print the dictionary on the screen.

dict4 = {
    'name': 'Erick',
    'age': 19,
    'height': [1.74, 18]
}
print(dict4)

# Exercise 9 - Create a list of 4 elements. The first element must be a string,
# the second a 2-element tuple, the third a dictionary with 2 keys and 2 values ​​and
# the fourth element a value of type float.
# Print the list on the screen.

list3 = ['Erick',
         (1, 2),
         {'key1': 'value1',
          'key2': 'value2'},
         1.74]
print(list3)

# Exercise 10 - Consider the string below. Print on the screen only characters from position
#  1 to 18.

phrase = 'Data Scientist is the Sexiest Professional of the 21st Century'
print(phrase[0:18])
