import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = data['Primary Fur Color']
sample = {}

for color in colors:
    if color not in sample.keys():
        sample[color] = 1
    sample[color] += 1

with open("color.csv", 'w') as file:
    file.write("Color, Number\n")
    for key, value in sample.items():
        file.write(str(key) + ',' + str(value)+'\n')
