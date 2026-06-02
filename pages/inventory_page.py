from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):
    # Локаторы
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[text()="Add to cart"]')

    @allure.step('Открыть корзину')
    def open_cart(self):
        self.click(self.CART_ICON)
        return self

    @allure.step('Добавить первый товар в корзину')
    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    @allure.step('Проверить, что страница каталога загружена')
    def should_be_loaded(self):
        assert 'inventory.html' in self.driver.current_url
        title_text = self.get_text(self.PRODUCTS_TITLE)
        assert title_text == 'Products'
        return self