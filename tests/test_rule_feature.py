import logging

import pytest

from config import Config

from pages.canvas_accountpage import CanvasAccountPage
from pages.canvas_loginpage import CanvasLoginPage
from pages.homepage import Homepage

logger = logging.getLogger(__name__)


@pytest.mark.regression
@pytest.mark.smoke
def test_invalid_uname_valid_password(driver):
    """
    Test case for verifying login functionality with an invalid username and a valid password.

    Steps:
    1. Navigate to the Instructure homepage.
    2. Navigate to the login menu and select the Canvas link.
    3. Select the Canvas network.
    4. Attempt to login with invalid credentials (invalid username and valid password).
    5. Verify that the appropriate error message is displayed.

    Assertions:
    - The error message should indicate message Please verify your username or password and try again. Trouble logging in.
    """

    home_page = Homepage(driver, Config.EXPLICIT_WAIT)
    canvas_login_page = CanvasLoginPage(driver, Config.EXPLICIT_WAIT)
    canvas_account_page = CanvasAccountPage(driver, Config.EXPLICIT_WAIT)

    # 1. Navigate to Instructure homepage
    home_page.navigate_to(Config.APP_URL)
    logger.info("Navigated to Instructure homepage")
    # 2. Navigate to login menu and select canvas link
    home_page.select_canvas_link()

    # 3. Select Canvas network
    canvas_account_page.click_canvas_network()

    # 5. Login with invalid credentials
    canvas_account_page.click_login_button(
        Config.INVALID_USERNAME, Config.VALID_PASSWORD
    )

    logger.info("Entered credentials and clicked Login button")
    # 6. Verify error message
    actual_error_message = canvas_login_page.get_flash_error_message()

    expected_error_message = (
        "Please verify your username or password and try again. Trouble logging in?"
    )

    # 7. Assert the error message
    assert (
        expected_error_message in actual_error_message
    ), f"Expected '{expected_error_message}',but got '{actual_error_message}'"


def test_empty_uname_empty_password(driver):
    """
    Test case for attempting to log in with empty username and password.

    Steps:
    1. Navigate to Instructure homepage.
    2. Navigate to login menu and select canvas link.
    3. Select Canvas network.
    4. Click the login button without entering credentials.
    5. Verify the error message displayed.

    Asserts:
    - The error message should indicate that no password was given.
    
    """

    logger.info("Starting test_empty_uname_empty_password")
    home_page = Homepage(driver, Config.EXPLICIT_WAIT)
    canvas_login_page = CanvasLoginPage(driver, Config.EXPLICIT_WAIT)
    canvas_account_page = CanvasAccountPage(driver, Config.EXPLICIT_WAIT)

    # 1. Navigate to Instructure homepage
    home_page.navigate_to(Config.APP_URL)
    logger.info("Navigated to Instructure homepage")
    # 2. Navigate to login menu and select canvas link
    home_page.select_canvas_link()

    # 3. Select Canvas network
    canvas_account_page.click_canvas_network()

    # 5. Login with invalid credentials
    canvas_account_page.click_login_button()

    logger.info("Entered credentials and clicked Login button")
    # 6. Verify error message
    actual_error_message = canvas_login_page.get_flash_error_message()

    expected_error_message = "No password was given"

    # 7. Assert the error message
    assert (
        expected_error_message in actual_error_message
    ), f"Expected '{expected_error_message}',but got '{actual_error_message}'"
    logger.info("Ending test_empty_uname_empty_password")
