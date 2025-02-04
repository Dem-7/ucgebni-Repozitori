import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
url = "https://www.divan.ru/rostov-na-donu/category/svet"
driver.get(url)
time.sleep(10)

vacancies = driver.find_elements(By.CLASS_NAME, "LlPhw")
parsed_data = []

for vacancy in vacancies:
    try:
        nazvanie = vacancy.find_element(By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct").text
        tsena = vacancy.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
        link = vacancy.find_element(By.CSS_SELECTOR, "span").get_attribute("href")

        parsed_data.append([nazvanie, tsena, link])  # Убедитесь, что у вас есть данные для названия компании
    except Exception as e:
        print(f"Ошибка при парсинге вакансии: {e}")
        continue

driver.quit()

with open("hh.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара',  'Цена', 'Ссылка на товар'])  # Исправлено заголовок
    writer.writerows(parsed_data)