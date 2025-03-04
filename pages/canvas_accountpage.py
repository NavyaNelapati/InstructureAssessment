from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CanvasAccountPage(BasePage):
    """
    CanvasAccountPage class represents the account page of Canvas.
    """

    # Locators Dictionary
    LOCATORS = {
        "canvas_network_button": (By.LINK_TEXT, "Canvas Network"),
        "email_textbox": (By.ID, "edit-email--2"),
        "password_textbox": (By.ID, "edit-password--2"),
        "login_button": (By.ID, "edit-submit--2"),
    }

    CANVAS_ACCOUNT_URLPATH = "/canvas/login"

    def __init__(self, driver, timeout=None):
        """
        Initializes the CanvasAccountPage.

        Args:
            driver (WebDriver): The web driver instance used to interact with the web page.
            timeout (int, optional): The maximum time to wait for the page to load. Defaults to None.
        """
        super().__init__(driver, timeout)
        self.wait_for_page_load(timeout)

    def click_canvas_network(self):
        """
        Clicks on the Canvas Network button on the account page.

        This method waits until the URL contains the specified Canvas account URL path,
        then clicks on the Canvas Network button using the locator defined in the LOCATORS dictionary.
        """
        self.wait_for_url_contains(self.CANVAS_ACCOUNT_URLPATH)
        self.scroll_to_element(self.LOCATORS["canvas_network_button"])
        self.click_element(self.LOCATORS["canvas_network_button"])

    def enter_email(self, email):
        """
        Enters the provided email into the email text field.

        Args:
            email (str): The email address to be entered into the text field.
        """
        self.fill_text_field(self.LOCATORS["email_textbox"], email)

    def enter_password(self, password):
        """
        Enters the provided password into the password text field.

        Args:
            password (str): The password to be entered into the password text field.
        """
        self.fill_text_field(self.LOCATORS["password_textbox"], password)

    def click_login_button(self, email=None, password=None):
        """
        Clicks the login button after optionally entering email and password.

        Args:
            email (str, optional): The email address to enter. Defaults to None.
            password (str, optional): The password to enter. Defaults to None.

        Returns:
            None
        """
        if email:
            self.enter_email(email)
        if password:
            self.enter_password(password)
        self.click_element(self.LOCATORS["login_button"])
