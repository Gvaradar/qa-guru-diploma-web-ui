import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


@pytest.fixture
def driver(request):
    """Локальный запуск ChromeDriver с автоматической установкой"""

    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(30)
    driver.set_page_load_timeout(60)
    driver.base_url = os.getenv('BASE_URL', 'https://www.saucedemo.com')

    yield driver

    # Вложения в Allure
    allure.attach(
        driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG
    )

    allure.attach(
        driver.page_source,
        name='HTML Page Source',
        attachment_type=allure.attachment_type.HTML
    )

    driver.quit()