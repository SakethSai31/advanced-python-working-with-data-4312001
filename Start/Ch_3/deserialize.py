# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []


# TODO: open the CSV file for reading
with open("largequakes.csv","r") as csvfile:
    reader = csv.reader(csvfile)

    #Check if Headers - > csv has an object module called sniffer
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024)
    csvfile.seek(0)

    if (sniffer.has_header(sample)):
        next(reader)

    for row in reader:
        # print(row[0])
        result.append(
            {
                "place": row[0],
                "magnitude": row[1],
                "link": row[2],
                "date": row[3]

            }
        )


print(result)
