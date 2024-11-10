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

# series is equivalent to a column in a table
data_dict = data.to_dict() # This will convert the data to a dictionary
print(data_dict)

# Convert the temperature column to a list
temp_list = data["temp"].to_list()
print(temp_list)

# average sum of the temperature
average_temp = data["temp"].mean()
print(average_temp)



