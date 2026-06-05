import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открыть страницу {url}")
    def open(self, url: str):
        """Открывает указанный URL"""
        self.driver.get(url)
        return self

    def find(self, locator: tuple):
        """Находит один элемент по локатору"""
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        """Находит все элементы по локатору"""
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple):
        """Клик по элементу"""
        self.find(locator).click()
        return self

    def type(self, locator: tuple, text: str):
        """Ввод текста в поле (с предварительной очисткой)"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator: tuple) -> str:
        """Возвращает текст элемента"""
        return self.find(locator).text

    def should_be_visible(self, locator: tuple):
        """Проверяет, что элемент видим на странице"""
        assert self.find(locator).is_displayed(), f"Элемент {locator} не видим"
        return self

    def wait_for_visible(self, locator: tuple):
        """Ожидает появления элемента на странице"""
        self.wait.until(EC.visibility_of_element_located(locator))
        return self

    def wait_for_clickable(self, locator: tuple):
        """Ожидает, когда элемент станет кликабельным"""
        self.wait.until(EC.element_to_be_clickable(locator))
        return self
