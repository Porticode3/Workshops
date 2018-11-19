'''
Functions are named blocks of code designed to do
one specific job. Functions allow you to write code
once that can then be run whenever you need to
accomplish the same task. Functions can take in the
information they need, and return the information they
generate. Using functions effectively makes your
programs easier to write, read, test, and fix.
'''

# Passing a single argument

def greet_user(username):
	print('Hello, ' + username + '!')

greet_user('Jesse')
greet_user('Quintin')

# Using propositional arguments

def describe_pet(animal, name):
	print("\nI have a " + animal + ".")
	print("Its name is " + name + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'bimbo')

print('\n')

# Returning a single value

def get_full_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()

musician = get_full_name('Jimi', 'Hendrix')
print (musician)

print('\n')

# Passing a list as an argument

def greet_users(names):
	for name in names:
		msg = "Hello, " + name + "!"
		print(msg)

names = ['Hannibal', 'Keith', 'Barry']
greet_users(names)

# Passing an arbitrary number of arguments
'''
Sometimes you won't know how many arguments a
function will need to accept. Python allows you to collect an
arbitrary number of arguments into one parameter using the
* operator. A parameter that accepts an arbitrary number of
arguments must come last in the function definition.
 The ** operator allows a parameter to collect an arbitrary
number of keyword arguments
'''

def make_pizza(size, *toppings):
	print ('\nMaking a ' + size + ' pizza.')
	print ( 'Toppings: ')
	for topping in toppings:
		print ('- ' + topping)

make_pizza('small', 'mushrooms')
make_pizza('medium', 'red peppers', 'sweetcorn')
make_pizza('large', 'onions', 'extra cheese')

# What's the best way to structure a function?

'''
As you can see there are many ways to write and call a
function. When you're starting out, aim for something that
simply works. As you gain experience you'll develop an
understanding of the more subtle advantages of different
structures such as positional and keyword arguments, and
the various approaches to importing functions. For now if
your functions do what you need them to, you're doing well.
'''

# Modules 
'''
You can store your functions in a separate file called a
module, and then import the functions you need into the file
containing your main program. This allows for cleaner
program files. (Make sure your module is stored in the
same directory as your main program.)
'''

# Storing a function in a module
# File: pizza.py

def make_pizza(size, *toppings):
	print ('\nMaking a ' + size + ' pizza.')
	print ( 'Toppings: ')
	for topping in toppings:
		print ('- ' + topping)

# Importing an entire module
# File: making_pizzas.py

import pizza
pizza.make_pizza('medium', 'jalapenos')
pizza.make_pizza('extra large', 'pepperoni')

# Also option to import a specific function
from pizza import make_pizza
pizza.make_pizza('medium', 'jalapenos')
pizza.make_pizza('extra large', 'pepperoni')

# Importing all fucntions from a module
'''
Don't do this, but recognize it when you see it in others' code. 
It can result in naming conflicts, which can cause errors.
'''

from pizza import *
pizza.make_pizza('medium', 'jalapenos')
pizza.make_pizza('extra large', 'pepperoni')

