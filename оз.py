from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Запуск драйвера
driver = webdriver.Chrome()
url = "https://www.divan.ru/rostov-na-donu/category/divany"
driver.get(url)

# Явное ожидание загрузки элементов
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "LlPhw")))

# Поиск элементов
loo = driver.find_elements(By.CLASS_NAME, "LlPhw")
parsed_data = []

for tt in loo:
    try:
        tsena = tt.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text

        if tsena:  # Проверка на пустые значения
            # Убираем "руб." и преобразуем в число
            tsena_numeric = float(tsena.replace("руб.", "").replace(" ", "").strip())
            parsed_data.append([tsena_numeric])
    except Exception as e:
        print(f"Ошибка парсинга: {e}")

# Закрытие драйвера
driver.quit()

# Запись данных в CSV
with open("rrr.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)

dd = pd.read_csv('rrr.csv')

print(f"Средняя цена - {dd['Цена'].mean()}")
plt.figure(figsize=(10, 6))
plt.hist(dd['Цена'], bins=20, edgecolor='black')
plt.title('Распределение цен диванов')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.show()
