import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()
url = "https://www.divan.ru/rostov-na-donu/category/svet"
driver.get(url)
time.sleep(10)
vacancies = driver.find_elements(By.CLASS_NAME, "LlPhw" )
print(vacancies)
parsed_data = []
for vacancy in vacancies:
    try:

        nazvanie = vacancy.find_element(By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct ").text
        tsena = vacancy.find_element(By.CSS_SELECTOR, "div.Dms7X.bluLL.Zpdfx ").text
        url = vacancy.find_element(By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct").get_attribute("href")
    except:
        print("Ошибка программы парсинга")
        continue
    parsed_data.append([nazvanie, tsena, url])
driver.quit()
with open("hh.csv", "w", newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Название ', 'Цена',  'ссылка '])
    writer.writerows(parsed_data)
















