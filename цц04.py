from random import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

q = webdriver.Chrome()
q.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
assert "Википедия" in q.title
a = input("Введите то, что хотите найти в википедии: ")

time.sleep(20)
gg = q.find_element(By.ID, "searchInput")
gg.send_keys(a)
gg.send_keys(Keys.RETURN)
time.sleep(20)
p = q.current_url

print('Выбирите дальнейший вариант ')
print(  "Листать параграфы текущей статьи - 1")
print("перейти на одну из связанных страниц - 2" )
print("Выйти  из программы - 3")
uu = input("Введите ваш вариант: ")
if uu == "1" :
    q.get(p)
    nn = q.find_elements(By.TAG_NAME, "p")
    for s in nn:
        print(s.text)
        input()
if uu == "2":
    q.get(p)
    hg = []
    for dd in  q.find_elements(By.TAG_NAME, "div"):
        dds = dd.get_attribute("class")
        if dds == "mw-disambig":
            hg.append(dd)

    ll = random.choice(hg)
    ffl = q.find_elements(By.TAG_NAME, "a").get_attribute("href")
    q.get(ffl)
    nn = q.current_url
    print("Хотите листать параграфы нажмите  1")
    print("перейти на одну из внутренних статей нажмите 2 ")
    mm = input("Введите данные")
    if mm == 1:
        q.get(nn)
        tt =q.find_elements(By.TAG_NAME, "p")
        for kjg in tt:
            print(kjg.text)
            input()

    if a == 2 :
        q.get(nn)
        tt = q.find_element(By.TAG_NAME, "a").get_attribute("href")
        nnd = random.choice(tt)
        q.get(nnd)

if uu == 3:
    q.quit()









