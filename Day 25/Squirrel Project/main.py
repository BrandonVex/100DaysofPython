import pandas 
data = pandas.read_csv("Day 25/Squirrel Project/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# to do
# create csv squirrel count that has small table that only obtains the squirrel color logged under primary fur color - cinnamon, gray, black
# how many grey, cinnamon, black ones pased on the column
# then we wil make a new data frame from it and create squirrel count.csv

# step 1 get the primary fur color column
data_primary_fur_color = data["Primary Fur Color"]

# step 2 count how many of each color there are
data_primary_fur_color_count = data_primary_fur_color.value_counts()

# step 3 create a new data frame from the data_primary_fur_color_count
data_primary_fur_color_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [data_primary_fur_color_count["Gray"], data_primary_fur_color_count["Cinnamon"], data_primary_fur_color_count["Black"]]
}

# create the new data frame from the code above
data_primary_fur_color_count_df = pandas.DataFrame(data_primary_fur_color_count_dict)

# step 4 save the data to a new csv file
data_primary_fur_color_count_df.to_csv("Day 25/Squirrel Project/squirrel_count.csv")