from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CanvasLoginPage(BasePage):
    """
    CanvasLoginPage class represents the login page for Canvas.
    """

    # Locators Dictionary
    LOCATORS = {
        "flash_message": (By.XPATH, "//body/div[@id='flash_message_holder']/div[1]"),
    }

    CANVAS_LOGIN_URLPATH = "/login/canvas"

    def __init__(self, driver, timeout=None):
        super().__init__(driver, timeout)
        self.wait_for_page_load(timeout)

    def get_flash_error_message(self):
        """
        Retrieves the flash error message displayed on the Canvas login page.

        Returns:
            str: The text of the flash error message.
        """
        self.wait_for_url_contains(self.CANVAS_LOGIN_URLPATH)
        message = self.get_element_text(self.LOCATORS["flash_message"])
        return message.strip()
