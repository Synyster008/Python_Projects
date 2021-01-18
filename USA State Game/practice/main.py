import pandas

data = pandas.read_csv('weather_data.csv')

monday = data[data.day == "Monday"]
monday_temp = (int(monday.temp)*1.8)+32
print(monday_temp)

