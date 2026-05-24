from selenium.webdriver.common.by import By
import allure

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')

    @allure.step('Заполнить форму оформления')
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
        return self

    @allure.step('Нажать Continue')
    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    @allure.step('Нажать Finish')
    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
        return self

    @allure.step('Проверить сообщение об успехе')
    def should_have_success_message(self):
        header = self.driver.find_element(*self.COMPLETE_HEADER)
        assert 'Thank you for your order' in header.text
        return self