def greet_user(username):
	print('Hello ' + username)

greet_user('Jesse')
greet_user('Quintin')

def describe_pet(animal, name):
	print('\nI have a ' + animal + '.')
	print('Its name is ' + name + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'bimbo')

print('\n')

def greet_users(names):
	for name in names:
		msg = "Hello, " + name + "!"
		print(msg)

names = ['Boris', 'Theresa', 'Jeremy']

greet_users(names)