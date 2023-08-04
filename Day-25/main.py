# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)


# import csv #<-- in built csv reader

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# #print(type(data)) # --> Pandas dataframe object
# #print(type(data["temp"])) #--> Series which is the equivalent of a list, like a single column\\

# data_dict = data.to_dict()
# print(data_dict) #--> creates a dictionary for each columnn

# temp_list = data["temp"].to_list() #--> converts to a python list
# print(temp_list)
# ## Average

# temp_series = data["temp"]
# # Alternatively can use data.temp
# print(f"Average is {temp_series.mean()}")

# ## max value in a column
# print(data["temp"].max())

# #Get data that is in the row
# monday = data[data.day == "Monday"]
# #print(data[data.temp == data.temp.max()])

# monday_temp = int(monday.temp)
# temp_farh = (monday_temp * 9/5) + 32
# print(temp_farh)

# #Create datafram from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# # my implementation
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# counts = list(data['Primary Fur Color'].value_counts())
# print(counts)

# data_dict = {
#     "Fur Color": ["gray", "red", "black"],
#     "Count": counts
# }

# squirrel_count = pandas.DataFrame(data_dict)
# squirrel_count.to_csv("squirrel_count.csv")

## udemy implementation
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_udemy.csv")
