from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    @allure.step('Открыть страницу логина')
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step('Ввести логин: {username}')
    def set_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        return self

    @allure.step('Ввести пароль')
    def set_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    @allure.step('Нажать кнопку Login')
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    @allure.step('Выполнить вход с логином {username} и паролем')
    def login(self, username: str, password: str):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        return self

    @allure.step('Проверить сообщение об ошибке')
    def should_have_error(self, expected_text: str):
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        assert expected_text in error.text
        return self