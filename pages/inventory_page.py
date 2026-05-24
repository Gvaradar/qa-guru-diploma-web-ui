from selenium.webdriver.common.by import By
import allure


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[text()="Add to cart"]')

    @allure.step('Открыть корзину')
    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
        return self

    @allure.step('Добавить первый товар в корзину')
    def add_first_item_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        return self

    @allure.step('Проверить, что страница каталога загружена')
    def should_be_loaded(self):
        assert 'inventory.html' in self.driver.current_url
        title = self.driver.find_element(*self.PRODUCTS_TITLE)
        assert title.text == 'Products'
        return self