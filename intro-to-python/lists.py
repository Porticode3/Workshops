users = ['Jack', 'Ronda', 'Polly', 'James']

first_user = users[0]
second_user = users[1]
last_user = users[-1]

users[2] = 'Pam'

users.append('Kim')

del users[2]

users.remove('James')

num_users = len(users)

print ("We have " + str(num_users) + " users.")

users.sort(reverse = True)
users.reverse()

for user in users:
	print(user)

for number in range(0, 101, 5):
	print(number)

numbers = list(range(1, 101))
print(numbers)

ages = [93, 23, 45, 72, 4, 1, 45, 68, 56, 91, 58]
youngest = min(ages)
oldest = max(ages)
total = sum(ages)

# Slicing 

lecturers = ['Graham', 'Robin', 'James', 'Mark', 'Dean', 'Yun', 'Kevin']
first_three = lecturers[:3]
middle_three = lecturers[1:4]
last_three = lecturers[-3:]

# Copy a list
copy_lecturers = lecturers[:]

# List comprehension

squares1 = []

for x in range(1, 11):
	square = x**2
	squares1.append(square)

print(squares1)

squares2 = [x**2 for x in range(1, 11)]

print(squares2)
