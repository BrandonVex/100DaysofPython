import csv
import pandas

# Open the CSV file
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    
# Using the pandas library
pandas.read_csv("weather_data.csv") # This is the same as the code above
print(data) # This will print the data in a table format

print(data["temp"]) # This will print the temperature column