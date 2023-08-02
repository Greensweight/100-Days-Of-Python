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

data = pandas.read_csv("weather_data.csv")
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

#Get data that is in the row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
