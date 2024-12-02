import pandas

data = pandas.read_csv("Day 25/weather_data.csv")
print(data)

# this converts the data into a dictionary for you can use it in a different way
data_dict = data.to_dict()
print(data_dict)

# temperature column is a series converted to a list
temp_list = data["temp"].to_list()
print(temp_list)

# average temperature
average_temp = data["temp"].mean()
print(average_temp)

# maximum temperature
max_temp = data["temp"].max()
print(max_temp)

# get data in column by index - condition is the column name
# they have to match identically with the column name in csv
print(data["condition"])
# data.condition works the same as stated above
print(data.condition)

# get an entire data row inside a row by index
# monday is the row we want inside the day index
print(data[data.day == "Monday"])
# this has a condition of the highest temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# convert Monday temperature to Fahrenheit
# we have to get the temperature value first by indexing it at 0 without the index the code will return a series
# then use the correct formula to convert it to Fahrenheit
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
    "grades": ["A", "B", "A"],
    "height": [1.65, 1.75, 1.80],
    "weight": [55, 70, 65],
}

# this will create a dataframe from the data_dict class above
data = pandas.DataFrame(data_dict)

# save to csv into a path
data.to_csv("Day 25/new_data.csv")