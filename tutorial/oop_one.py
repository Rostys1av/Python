"""
Classes - Blueprint
Object - The house (built from blueprint)
Objects have properties and methods (functions)
Use "class" keyword (Convection to start from capital letter)
__init__ use to initialize all objects we'll create with car class. Called a magic method for a special purposes self in the first parameter passed in Python
"""

class Computers: #this is creating new class
    def __init__(self, name , color, os): # These are called instance variables or attributes
        self.name = name
        self.color = color
        self.os = os
    def start(self):
        print("Starting my " + self.name + " PC")
    def re_start(self):
        print("Re-starting my " + self.name + " PC")
    def shut_down(self):
        print("Shutting down " + self.name + " PC")
    def email(self):
        print("This method prints an email from the parent class")

class TableComputers(Computers):
    def __init__(self):
        Computers.__init__(self, name="Asus", color="Black", os="Unix")
        print("This is tablet computer class __init__ method")
    def download(self):
        print("Download tablet apps")
    def email(self):
        super(TableComputers, self).email()
        print("This method overrides email function from Parent class")

table_comp = TableComputers()
table_comp.start()
table_comp.re_start()
table_comp.shut_down()
table_comp.email()

table_comp1 = TableComputers()
table_comp1.download()

print("------------------")

apple = Computers("Apple", "gray", "MacOS") #This is instantiate a class (creating an object)
print(apple.name)
print(apple.color)
print(apple.os)
apple.start()
apple.re_start()
apple.shut_down()
apple.email()

print("------------------")

hp = Computers("HP","Blue","Windows")
print(hp.name)
print(hp.color)
print(hp.os)
hp.start()
hp.re_start()
hp.shut_down()

print("------------------")

dell = Computers("Dell","White","Unix")
print(dell.name)
print(dell.color)
print(dell.os)
dell.start()
dell.re_start()
dell.shut_down()