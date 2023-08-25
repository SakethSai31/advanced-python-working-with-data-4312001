# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime
import pprint


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def sig_events(q):
    significane = q["properties"]["sig"]
    return 0 if significane is None else significane


#significant_events = list(filter(sig_events, data["features"]))

significant_events = sorted(data["features"], key=sig_events, reverse=True)
significant_events = significant_events[:40]
significant_events.sort(key=lambda e: e["properties"]["time"], reverse=True)


# def googleMap_url(q):
#     lat = q["geometry"]["coordinates"][0]
#     lon = q["geometry"]["coordinates"][1]
#     gmap_url = str(
#         f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{lon}")
#     return gmap_url


# all_map_events = list(map(googleMap_url, data["features"]))


headers = ["Magnitude", "Place", "Felt", "Date", "Google Map Link"]
rows = []


for event in significant_events:
    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"])/1000
    )
    lat = event["geometry"]["coordinates"][0]
    lon = event["geometry"]["coordinates"][1]
    gmap_url = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{lon}"

    rows.append([
        event["properties"]["mag"],
        event["properties"]["place"],
        0 if event["properties"]["felt"] is None else event["properties"]["felt"],
        thedate,
        gmap_url
    ])

with open ("significantevents.csv", "w", ) as csv_file:

    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(headers)
    writer.writerows(rows)
