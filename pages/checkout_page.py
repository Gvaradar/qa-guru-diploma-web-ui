from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')
    CANCEL_BUTTON = (By.ID, 'cancel')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    @allure.step('Заполнить форму оформления')
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        return self

    @allure.step('Нажать Continue')
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
        return self

    @allure.step('Нажать Finish')
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
        return self

    @allure.step('Проверить сообщение об успехе')
    def should_have_success_message(self):
        header = self.find(self.COMPLETE_HEADER)
        assert 'Thank you for your order' in header.text
        return self

    @allure.step("Нажать Cancel")
    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)
        return self

    @allure.step("Проверить, что на странице корзины")
    def should_be_on_cart_page(self):
        assert 'cart.html' in self.driver.current_url
        return self

    @allure.step("Проверить сообщение об ошибке: {expected_text}")
    def should_have_error_message(self, expected_text: str):
        error = self.find(self.ERROR_MESSAGE)
        assert expected_text in error.text
        return self