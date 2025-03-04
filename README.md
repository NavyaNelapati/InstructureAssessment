# Instructure Assessment

This project is an automated testing suite for the Canvas web application. It uses Selenium WebDriver for browser automation and Pytest for test execution.

## Project Structure

The project directory is organized as follows:

```
InstructureAssessment/
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── test_login_feature.py
│   └── test_dashboard_feature.py
├── utils/
│   ├── helpers.py
│   └── logger.py
├── config.py
├── requirements.txt
├── README.md
└── reports/
    └── test_report.html
```

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/InstructureAssessment.git
    cd InstructureAssessment
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file with the necessary configuration details such as valid and invalid usernames and passwords.

## Running Tests

To run the all tests under tests module, use the following command:
```sh
python -m pytest tests --html=reports/test_report.html
```

You can also run specific tests:
```sh
python -m pytest tests/test_login_feature.py --html=reports/test_report.html
```
To Run Regression and/or Smoke tests:
```sh
python -m pytest -m "smoke or regression"
```

## Logging
Logging is configured to capture important events and errors. Logs can be found in the logs directory. Log level is set to ERROR.