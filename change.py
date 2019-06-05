import pandas as pd

dataset = pd.read_csv('data/ipl.csv')

l = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 'Deccan Chargers', 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Delhi Daredevils', 'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Gujarat Lions', 'Rising Pune Supergiant']

for i in range(0, len(l)):
	dataset.loc[dataset["bat_team"]==l[i], "bat_team"] = i
	dataset.loc[dataset["bowl_team"]==l[i], "bowl_team"] = i

dataset.to_csv("data/ipl.csv", index=False)