from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')

    @allure.step('Нажать кнопку Checkout')
    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self

    @allure.step('Проверить, что в корзине {expected_count} товар(ов)')
    def should_have_items_count(self, expected_count: int):
        items = self.driver.find_elements(*self.CART_ITEM)
        assert len(items) == expected_count
        return self