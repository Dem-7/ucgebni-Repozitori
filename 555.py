print("Задание 1")
import numpy as np
import matplotlib.pyplot as nn
data = np.random.normal(0, 1, 100)
nn.hist(data, bins=4)
nn.xlabel("ось x")
nn.xlabel("ось y")
nn.title("гистограммa случайных данных")
nn.show()

print("Задание 2")
random_array = np.random.rand(5)
array = np.random.rand(5)
nn.scatter(random_array,array)
nn.title("Диаграмма рассеивания")
nn.xlabel("ось x")
nn.xlabel("ось y")
nn.show()






