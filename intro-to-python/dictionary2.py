users = []

new_user = {
	'first' : 'Jack',
	'last' : 'Morrison', 
	'username' : 'Soldier76'
}
users.append(new_user)

new_user = {
	'first' : 'Jesse',
	'last' : 'McCree', 
	'username' : 'McCree64'
}
users.append(new_user)

# show all information

for user_dict in users:
	for k, v in user_dict.items():
		print (k + ': ' + v)
	print('\n')