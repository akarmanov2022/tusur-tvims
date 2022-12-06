import csv
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(array: [], title: str, x_label: str, y_label: str, bins: int):
    plt.hist(array, bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def load_data_from_csv(filename: str) -> []:
    csv_data = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            value = int(row[1])
            csv_data.append(value)
    return csv_data


data = load_data_from_csv('W2.csv')
print('Данные из файла: \n', data)
data.sort()
print('Отсортированные данные в порядке возрастания: \n', data)
min_value = data[0]
print('Минимальное значение: ', min_value)
max_value = data[-1]
print('Максимальное значение: ', max_value)
scope = max_value - min_value
print('Размах: ', scope)

# Нахождение количества групп
length = len(data)
print('Количество элементов: ', length)
number_of_groups = round(1 + 3.322 * np.log10(length))
print('Количество групп: ', number_of_groups)
interval = scope / number_of_groups
print('Ширина интервала: ', interval)

# Рассчет интервалов
intervals = []
for i in range(int(number_of_groups)):
    intervals.append((min_value + i * interval, min_value + (i + 1) * interval))
print('Интервалы: \n', intervals)

# Рассчет вектора-столбца средних значений интервалов
mean_column = []
for interval in intervals:
    mean_column.append((interval[0] + interval[1]) / 2)
print('Вектор-столбец средних значений интервалов: ', mean_column)

sample_mean = sum(data) / len(data)
print('Выборочное среднее: ', sample_mean)

median = 0
if length % 2 == 0:
    median = (data[length // 2 - 1] + data[length // 2]) / 2
else:
    median = data[length // 2]
print('Медиана: ', median)

sample_variance = sum([(x - sample_mean) ** 2 for x in data]) / len(data)
print('Выборочная дисперсия: ', sample_variance)

standard_deviation = sample_variance ** (1 / 2)
print('Среднеквадратическое отклонение: ', standard_deviation)

sampling_moment_3 = sum([(x - sample_mean) ** 3 for x in data]) / len(data)
print('Выборочный момент третьего порядка: ', sampling_moment_3)

sampling_moment_4 = sum([(x - sample_mean) ** 4 for x in data]) / len(data)
print('Выборочный момент четвертого порядка: ', sampling_moment_4)

selective_kurtosis = sampling_moment_4 / (standard_deviation ** 4) - 3
print('Выборочный эксцесс: ', selective_kurtosis)

# Оценка асимметрии
asymmetry = sampling_moment_3 / (standard_deviation ** 3)
print('Асимметричность: ', asymmetry)

# Отображение гистограммы
plot_histogram(data, 'Гистограмма', 'Значения', 'Частота', number_of_groups)
