

from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
import random
browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
aa =  []
ss = browser.find_elements(By.TAG_NAME, "div")
for d in ss:
    jj = d.get_attribute("class")
    if jj =="hatnote navigation-not-searchable":
        aa.append(d)
print(aa)
s = random.choice(aa)
nn = s.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(nn)
