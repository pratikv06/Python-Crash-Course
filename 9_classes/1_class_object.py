# Dog module
# class keyword is uesd to describe class
# class name should be in CamelCase

class Dog():
    """A simple attempt to model a dog"""
    # A function that is a part of class is called `method`
    # `init` method special method
    # two leading and tailing underscore
    # Run automatically whenever class instance is created
    # `self` parameter is required, first before any other parameter
    # self refer to instance of itself
    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age
    
    
    # Instance have access to this method
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() +" is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() +" rolled over!!")

    # End of the class

print(">> Creating object of the class:")
my_dog = Dog('willie', 6)
print(type(my_dog))
print(">> Let create one more object:")
your_dog = Dog('lucy', 3)
print(type(your_dog))

print("\n>> Accessing attribute of class:")
# we can access attribute by objectname.attributename
print("My dog's name is "+ my_dog.name.title() +".")
print("My dog is "+ str(my_dog.age) +" years old.")


print("\n>> Calling a method of the class:")
# we can access method using objectname.methodname()
my_dog.sit()
my_dog.roll_over()

print("\n>> displaying second object value")
print("My dog's name is "+ your_dog.name.title() +".")
print("My dog is "+ str(your_dog.age) +" years old.")
your_dog.sit()
your_dog.roll_over()