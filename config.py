import os


class Config:

    # URLS
    APP_URL = "https://www.instructure.com/"

    # CREDS
    INVALID_USERNAME = "invalid_email@gmail.com"
    INVALID_PASSWORD = "ncdhc@892912"

    VALID_USERNAME = "username@gmail.com"
    VALID_PASSWORD = "valid_password"

    # BROWSER OPTIONS
    BROWSER = os.environ.get("BROWSER", "chrome")  # chrome, safari
    HEADLESS = int(os.environ.get("HEADLESS", 1))

    # TIMEOUTS
    IMPLICIT_PAGE_TIMEOUT = int(os.environ.get("IMPLICIT_PAGE_TIMEOUT", 15))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT", 20))
