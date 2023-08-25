# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
# 1: How many quakes are there in total?

print("Total Quakes: ", len(data["features"]))

# 2: How many quakes were felt by at least 100 people?

print("Total quakes felt by at least 100 people: ",sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in data["features"]))

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports


def getfelt(q):
    f = q["properties"]["felt"]
    if f is None:
        f = 0
    return float(f)

max_felt = max(data["features"], key=getfelt)

print("Most Felt reports:", "Mag:", max_felt["properties"]["mag"] , "-",
 max_felt["properties"]["place"], "reports:", max_felt["properties"]["felt"] )

# 4: Print the top 10 most significant events, with the significance value of each

def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0

sigevents = sorted(data["features"], key= getsig, reverse=True)
print("The 10 most significant events are: ")
for i in range (0,10):
    print (
        f'Event Name: {sigevents[i]["properties"]["title"]}, Significance: {sigevents[i]["properties"]["sig"]}'
        )
