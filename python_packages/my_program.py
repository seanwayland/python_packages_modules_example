from datetime import datetime
import my_package
from my_package import Person as p
# print(datetime)
# #print(dir(datetime))
# print("hello")

# t = datetime
# print(t)
# print(t.now())

# print(my_package.todays_day)
# print(my_package.yesterday)
# print(my_package)

# my_package.print_todays_day()

### create an object which is of type "Person" class 
### use the class "constructor" called __init__ in the python language 
### pass the name and age into the constructor 
### this creates a Person "object" with a name "john and an age 36 "
john =  p("John", 36)

### print the variable called "name" from the Person object calld "john"
print(john.name)
### print the variable called "age" from the Person object calld "john"
print(john.age)

bob = p("Bobbo", 45)

print(bob.name)
print(bob.age)


#### call the "make_older" method which adds years to the variable called age for that Person 
### we are calling this method with an argument of 5 

bob.make_older(5)
print(bob.age)

john.make_older(10)
print(john.age)