import requests

person_number = input("Please enter the person's number: ")

r = requests.get("https://swapi.co/api/people/" + person_number)

data = r.json()

print("*** Person Profile ***")
print("Name: \t\t" + data['name'])
print("Height: \t{}cm".format(data['height']))
print("Mass: \t\t{}kg".format(data['mass']))

print("Films they were in")
for film in data['films']:
    print("Film information available at: " + film)
