from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на главную страницу Википедии
    driver.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in driver.title

    # 1. Спрашиваем у пользователя первоначальный запрос
    search_query = input("Введите запрос для поиска в Википедии: ")

    # 2. Выполняем поиск по запросу
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchInput"))
    )
    search_input.send_keys(search_query)
    search_input.send_keys(Keys.RETURN)

    # Ожидаем загрузки результатов поиска
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )

    while True:
        # 3. Предлагаем пользователю три варианта действий
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        user_choice = input("Введите номер действия: ")

        if user_choice == "1":
            # Листаем параграфы текущей статьи
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input("Нажмите Enter, чтобы продолжить...")

        elif user_choice == "2":
            # Получаем список всех ссылок на странице
            all_links = driver.find_elements(By.TAG_NAME, "a")
            valid_links = [link.get_attribute("href") for link in all_links if link.get_attribute("href")]

            if not valid_links:
                print("На странице нет доступных ссылок.")
                continue

            # Выбираем случайную ссылку
            selected_link = choice(valid_links)
            driver.get(selected_link)

            # После перехода предлагаем два варианта
            while True:
                print("\nВыберите действие:")
                print("1. Листать параграфы текущей статьи")
                print("2. Перейти на одну из внутренних статей")
                sub_choice = input("Введите номер действия: ")

                if sub_choice == "1":
                    # Листаем параграфы текущей статьи
                    paragraphs = driver.find_elements(By.TAG_NAME, "p")
                    for paragraph in paragraphs:
                        print(paragraph.text)
                        input("Нажмите Enter, чтобы продолжить...")
                    break  # Возвращаемся к основному меню

                elif sub_choice == "2":
                    # Переходим на одну из внутренних статей
                    all_links = driver.find_elements(By.TAG_NAME, "a")
                    valid_links = [link.get_attribute("href") for link in all_links if link.get_attribute("href")]

                    if not valid_links:
                        print("На странице нет доступных ссылок.")
                        break

                    selected_link = choice(valid_links)
                    driver.get(selected_link)

                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif user_choice == "3":
            # Выходим из программы
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

finally:
    # Закрываем браузер при выходе
    driver.quit()