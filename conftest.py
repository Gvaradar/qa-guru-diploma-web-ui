import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture
def driver(request):
    """Фикстура для настройки драйвера"""
    options = Options()
    options.add_argument('--window-size=1920,1080')

    # Пока локальный запуск, позже добавим Selenoid
    driver = webdriver.Chrome(options=options)

    # Базовый URL
    base_url = 'https://www.saucedemo.com'
    driver.base_url = base_url

    def fin():
        # Добавляем вложения в Allure
        allure.attach(
            driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
        driver.quit()

    request.addfinalizer(fin)
    return driver