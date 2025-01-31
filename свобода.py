from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация веб-драйвера
q = webdriver.Chrome()
q.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
assert "Википедия" in q.title

# Запрос первоначального запроса у пользователя
a = input("Введите то, что хотите найти в Википедии: ")

# Поиск статьи
gg = q.find_element(By.ID, "searchInput")
gg.send_keys(a)
gg.send_keys(Keys.RETURN)
time.sleep(2)  # Ожидание загрузки страницы

# Получение текущего URL
p = q.current_url

while True:
    print('Выберите дальнейший вариант:')
    print("Листать параграфы текущей статьи - 1")
    print("Перейти на одну из связанных страниц - 2")
    print("Выйти из программы - 3")
    uu = input("Введите ваш вариант: ")

    if uu == "1":
        # Листаем параграфы текущей статьи
        q.get(p)
        nn = q.find_elements(By.TAG_NAME, "p")
        for s in nn:
            print(s.text)
            input("Нажмите Enter, чтобы продолжить...")

    elif uu == "2":
        # Переход на связанные страницы
        q.get(p)
        hg = []
        for dd in q.find_elements(By.TAG_NAME, "div"):
            if "mw-disambig" in dd.get_attribute("class"):
                hg.append(dd)

        if hg:
            # Выбираем случайную связанную страницу
            ll = choice(hg)
            links = ll.find_elements(By.TAG_NAME, "a")  # Получаем ссылки
            if links:
                ffl = choice(links).get_attribute("href")  # Выбираем случайную ссылку
                q.get(ffl)
                nn = q.current_url

                print("Хотите листать параграфы? Нажмите 1")
                print("Перейти на одну из внутренних статей - нажмите 2")
                mm = input("Введите данные: ")

                if mm == "1":
                    # Листаем параграфы выбранной статьи
                    tt = q.find_elements(By.TAG_NAME, "p")
                    for kjg in tt:
                        print(kjg.text)
                        input("Нажмите Enter, чтобы продолжить...")

                elif mm == "2":
                    # Переходим на случайную внутреннюю статью
                    internal_links = q.find_elements(By.TAG_NAME, "a")
                    internal_links = [link.get_attribute("href") for link in internal_links if "/wiki/" in link.get_attribute("href")]
                    if internal_links:
                        nnd = choice(internal_links)
                        q.get(nnd)

    elif uu == "3":
        # Выход из программы
        q.quit()
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")