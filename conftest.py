import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


# ========== ФИКСТУРА ДЛЯ ПРОГРЕВА САЙТА ==========
@pytest.fixture(scope='session', autouse=True)
def wake_up_site():
    """Прогреваем сайт перед всеми тестами"""
    try:
        requests.get('https://www.saucedemo.com', timeout=10)
        print("✅ Сайт успешно прогрет")
    except:
        print("⚠️ Не удалось прогреть сайт, но продолжаем")


# ========== ОСНОВНАЯ ФИКСТУРА ДРАЙВЕРА ==========
@pytest.fixture
def driver(request):
    """Локальный запуск ChromeDriver с автоматической установкой"""

    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    # Автоматическая установка и запуск ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Настройки таймаутов
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(60)

    # Базовый URL
    driver.base_url = 'https://www.saucedemo.com'

    yield driver

    # ========== ВЛОЖЕНИЯ В ALLURE ==========

    # 1. Скриншот
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name='📸 Скриншот',
            attachment_type=allure.attachment_type.PNG
        )
    except:
        pass

    # 2. HTML страницы
    try:
        allure.attach(
            driver.page_source,
            name='📄 HTML страницы',
            attachment_type=allure.attachment_type.HTML
        )
    except:
        pass

    # Закрываем браузер
    driver.quit()