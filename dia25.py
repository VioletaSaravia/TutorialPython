""" Día 25 - Pandas"""

import pandas

data = pandas.read_csv("data.csv")
temperaturas = data["temp"]

data_dict = data.to_dict()
temperaturas_list = data["temp"].to_list()
# temperaturas_list = ['23','30','34','7','17','3','39']
promedio = sum(map(int, temperaturas_list)) / len(temperaturas_list)
print(promedio)

print(data["temp"].mean())      # o data.temp
print(data["temp"].max())

# Conseguir fila
print(data[data.day == "Monday"]) # monday es la fila, devuelve toda
print(data[data.temp == data.temp.max()])

monday_temp_f = int(data[data.day == "Monday"].temp) * 9/5 + 32

data_from_dict = pandas.DataFrame(data_dict)
data_to_csv = data.to_csv('new_data.csv')
