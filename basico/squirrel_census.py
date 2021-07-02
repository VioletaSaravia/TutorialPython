import pandas

data = pandas.read_csv("census_data.csv")
colores = data["Primary Fur Color"].to_list()

colors_count = {}
for color in colores:
    if color in colors_count.keys():
        colors_count[color] += 1
    else:
        colors_count[color] = 1

colors_count = pandas.DataFrame(colors_count, index=['Count'])
print(colors_count)
colors_count.to_csv("census_colours.csv")
