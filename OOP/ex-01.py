# Exercise 1 - Create an object from the class below, called roc1, passing 2 parameters and
# then make a call to attributes and methods

class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rocket(self):
        print(self.x, self.y)


roc1 = Rocket(10, 34)
roc1.x
roc1.y
roc1.print_rocket()
roc1.move_rocket(12, 44)
roc1.print_rocket()

# Exercise 2 - Create a class called Person() with attributes: name, city, telephone and e-mail. use
# at least 2 special methods in your class. Create an object of your class and make a call
# to at least one of its special methods.


class Person():

    def __init__(self, name, city, phone, email):
        self.name = name
        self.city = city
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Hi! your name is {self.name}, you live in {self.city}, your phone is {self.phone} and \
your email is {self.email}"

    def __len__(self):
        return self.phone


person1 = Person("Maria", "Limoeiro do Norte", 8899340997, "maria@gmail.com")
str(person1)
len(person1)

# Exercise 3 - Create the Smartphone class with 2 attributes, size and interface and create the MP3Player class
# with capacity attributes. The MP3player class must inherit the attributes of the Smartphone class.


class Smartphone(object):
    def __init__(self, size, interface):
        self.size = size
        self.interface = interface


class MP3player(Smartphone):
    def __init__(self, capacity, size='small', interface='led'):
        self.capacity = capacity
        Smartphone.__init__(self, size, interface)

    def printmp3(self):
        print(
            f"Values for object: {self.size} {self.interface} {self.capacity}")


device = MP3player("64GB")
device.printmp3()
