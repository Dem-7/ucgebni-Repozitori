import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
url = "https://www.divan.ru/rostov-na-donu/category/svet"
driver.get(url)
time.sleep(60)

loo = driver.find_elements(By.CLASS_NAME, "LlPhw")
parsed_data = []

for tt in loo:
    try:
        nazvanie = tt.find_element(By.CSS_SELECTOR, "a").text
        tsena = tt.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
        url = tt.find_element(By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct").get_attribute("href")
        parsed_data.append([nazvanie, tsena, url])
    except Exception as e:
        print(f"Ошибка при обработке элемента: {e}")

driver.quit()

with open("tt.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

