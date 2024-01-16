# with open('weather_data.csv') as data:
#     data_list  = data.readlines()
# print(data_list)

# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

df = pd.read_csv('weather_data.csv')
# print(df[df.temp==df.temp.max()])

# monday = df.iloc[0]
# fahrenheit = (monday.temp*9/5)+32
# print(fahrenheit)
new_data = pd.DataFrame({'student':['a','b','c'],
            'scores':['1','2','3']})
print(new_data)
df.to_csv("new_data.csv")
df['color']