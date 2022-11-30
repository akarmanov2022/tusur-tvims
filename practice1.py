import csv
import numpy as np


def load_data_from_csv(filename: str) -> np.array:
    csv_data = np.array([])
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            value = int(line[1])
            csv_data = np.append(csv_data, value)
    return csv_data


data = load_data_from_csv('W2.csv')
print('Данные из файла: \n', data)
data.sort()
print('Отсортированные данные в порядке возрастания: \n', data)
min_value = min(data)
print('Минимальное значение: ', min_value)
max_value = max(data)
print('Максимальное значение: ', max_value)
scope = max_value - min_value
print('Размах: ', scope)

# Рассчет по формуле Стерджесса
number_of_groups = int(1 + 3.322 * np.log10(len(data)))
print('Количество групп: ', number_of_groups)
interval = scope / number_of_groups
print('Ширина интервала: ', interval)

intervals = []
for i in range(int(number_of_groups)):
    intervals.append((min_value + i * interval, min_value + (i + 1) * interval))
print('Интервалы: ', intervals)



