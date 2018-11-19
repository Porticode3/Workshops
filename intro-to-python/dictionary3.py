# Store multiple languages for each person

fav_languages = {
 'jen': ['python', 'php'],
 'sarah': ['c', 'c++'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell', 'java'],
}

# Show all responses for each person

for name, langs in fav_languages.items():
 print(name + ": ")
 for lang in langs:
 	print("- " + lang)

# Storing a dictionary inside a dictionary
# Each value stored associated with a key is itself a dictionary

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_dict in users.items():
 print("\nUsername: " + username)
 full_name = user_dict['first'] + " "
 full_name += user_dict['last']
 location = user_dict['location']
 print("\tFull name: " + full_name.title())
 print("\tLocation: " + location.title())