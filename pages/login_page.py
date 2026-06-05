import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step("Ввести логин: {username}")
    def set_username(self, username: str):
        self.type(self.USERNAME_INPUT, username)
        return self

    @allure.step("Ввести пароль")
    def set_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)
        return self

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    @allure.step("Выполнить вход с логином {username}")
    def login(self, username: str, password: str):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        return self

    @allure.step("Проверить сообщение об ошибке")
    def should_have_error(self, expected_text: str):
        error_text = self.get_text(self.ERROR_MESSAGE)
        assert expected_text in error_text, f"Ожидалось '{expected_text}', получено '{error_text}'"
        return self

    @allure.step("Проверить, что открыта страница каталога")
    def should_be_on_inventory_page(self):
        assert 'inventory.html' in self.driver.current_url
        return self
