fav_team = {
	'Jacko' : 'Chelsea', 
	'Daniel' : 'Arsenal', 
	'Greg' : 'Tottenham', 
	'Ralph' : 'Man City'
}

for name, team in fav_team.items():
	print(name + ': ' + team)

for name in fav_team.keys():
	print(name)

for team in fav_team.values():
	print(team)

num_responses = len(fav_team)
print(num_responses)