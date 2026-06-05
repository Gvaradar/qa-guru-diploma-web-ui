import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(60)
    driver.set_page_load_timeout(120)
    driver.base_url = os.getenv('BASE_URL')

    yield driver

    allure.attach(
        driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG
    )
    allure.attach(
        driver.page_source,
        name='Page source',
        attachment_type=allure.attachment_type.HTML
    )

    driver.quit()