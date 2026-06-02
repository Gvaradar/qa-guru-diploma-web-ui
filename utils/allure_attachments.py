import allure


def attach_screenshot(driver, name="Screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def attach_html(driver, name="HTML Page Source"):
    allure.attach(
        driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.HTML
    )