import csv
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(array: np.array, title: str, x_label: str, y_label: str, bins: int) -> None:
    plt.hist(array, bins=bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


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

# Нахождение количества групп
number_of_groups = int(1 + 3.322 * np.log10(len(data)))
print('Количество групп: ', number_of_groups)
interval = scope / number_of_groups
print('Ширина интервала: ', interval)

# Рассчет
intervals = []
for i in range(int(number_of_groups)):
    intervals.append((min_value + i * interval, min_value + (i + 1) * interval))
print('Интервалы: ', intervals)

# Рассчет вектора-столбца средних значений интервалов
mean_column = []
for interval in intervals:
    mean_column.append((interval[0] + interval[1]) / 2)
print('Вектор-столбец средних значений интервалов: ', mean_column)

sample_mean = np.mean(data)
print('Выборочное среднее: ', sample_mean)

median = np.median(data)
print('Медиана: ', median)

sample_variance = np.var(data)
print('Выборочная дисперсия: ', sample_variance)

standard_deviation = np.std(data)
print('Среднеквадратическое отклонение: ', standard_deviation)

sampling_moment_3 = np.mean(data ** 3)
print('Выборочный момент третьего порядка: ', sampling_moment_3)

sampling_moment_4 = np.mean(data ** 4)
print('Выборочный момент четвертого порядка: ', sampling_moment_4)

selective_kurtosis = (sampling_moment_4 / (sample_variance ** 2)) - 3
print('Выборочная эксцесс: ', selective_kurtosis)

asymmetry_factor = (sampling_moment_3 / (sample_variance ** 1.5))
print('Асимметричность: ', asymmetry_factor)

histogram = np.histogram(data, number_of_groups)
hist = plt.hist(data, number_of_groups)

# Отображение гистограммы
plot_histogram(data, 'Гистограмма', 'Значения', 'Частота', number_of_groups)
