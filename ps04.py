from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Инициализация браузера
browser = webdriver.Chrome()  # Используйте webdriver.Firefox(), если работаете с Firefox

try:
    # Открываем главную страницу Википедии
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in browser.title  # Проверяем, что открылась нужная страница

    # Спрашиваем у пользователя запрос
    query = input("Введите то, что хотите найти в Википедии: ")

    # Вводим запрос в поисковую строку
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # Проверяем, куда нас перенаправило
    try:
        # Если мы сразу попали на статью, проверяем заголовок
        title = browser.find_element(By.ID, "firstHeading").text
        print(f"Перешли к статье: {title}")
    except:
        # Если мы на странице с результатами поиска, выбираем первый результат
        try:
            first_result = browser.find_element(By.XPATH, "//div[@class='mw-search-results']/ul/li[1]/div/a")
            first_result.click()
            time.sleep(5)
        except:
            print("Страница не найдена. Попробуйте другой запрос.")
            exit()

    # Основной цикл действий
    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Листаем параграфы текущей статьи
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for i, paragraph in enumerate(paragraphs):
                print(f"Параграф {i + 1}:")
                print(paragraph.text)
                input("Нажмите Enter для следующего параграфа...")

        elif choice == "2":
            # Переходим на одну из связанных страниц
            links = browser.find_elements(By.TAG_NAME, "a")
            valid_links = [link.get_attribute("href") for link in links if link.get_attribute("href") and "wiki" in link.get_attribute("href")]
            if not valid_links:
                print("Связанные страницы не найдены.")
                continue

            # Выбираем случайную ссылку
            random_link = random.choice(valid_links)
            print(f"Переходим по ссылке: {random_link}")
            browser.get(random_link)
            time.sleep(5)

            # Предлагаем пользователю два варианта действий
            while True:
                print("\nВыберите действие:")
                print("1. Листать параграфы текущей статьи")
                print("2. Вернуться к предыдущей странице")

                sub_choice = input("Введите номер действия: ")

                if sub_choice == "1":
                    # Листаем параграфы текущей статьи
                    paragraphs = browser.find_elements(By.TAG_NAME, "p")
                    for i, paragraph in enumerate(paragraphs):
                        print(f"Параграф {i + 1}:")
                        print(paragraph.text)
                        input("Нажмите Enter для следующего параграфа...")
                    break

                elif sub_choice == "2":
                    # Возвращаемся к предыдущей странице
                    browser.back()
                    time.sleep(5)
                    break

                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

finally:
    # Закрываем браузер
    browser.quit()