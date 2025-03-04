from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Homepage(BasePage):
    """
    Homepage class represents the home page of the application.

    Attributes:
        LOCATORS (dict): A dictionary containing locators for elements on the home page.

    Methods:
        __init__(driver, timeout=None):
            Initializes the home page and waits for it to load.

        click_login():
            Clicks the login link on the home page.

        select_canvas_link():
            Clicks the login link and then clicks the Canvas link on the home page.
    """

    # Locators Dictionary
    LOCATORS = {
        "login_link": (By.LINK_TEXT, "Log In"),
        "canvas_link": (By.XPATH, "//a[contains(text(),'Canvas')]"),
    }

    def __init__(self, driver, timeout=None):
        """
        Initialize the home page.

        Args:
            driver (WebDriver): The WebDriver instance to interact with the browser.
            timeout (int, optional): The maximum time to wait for the page to load. Defaults to None.
        """
        super().__init__(driver, timeout)
        self.wait_for_page_load(timeout=timeout)

    def click_login(self):
        """
        Clicks the login link on the homepage.

        This method locates the login link using the locator defined in the LOCATORS dictionary
        and performs a click action on it.
        """
        self.click_element(self.LOCATORS["login_link"])

    def select_canvas_link(self):
        """
        Selects the Canvas link on the homepage.

        This method performs the following actions:
        1. Clicks the login button.
        2. Clicks the Canvas link element.
        """
        self.click_login()
        self.click_element(self.LOCATORS["canvas_link"])
