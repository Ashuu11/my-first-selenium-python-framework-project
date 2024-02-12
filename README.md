# My First Selenium Python Framework

## Introduction

Welcome to "My First Selenium Python Framework" project! This repository serves as a starting point for building a basic Selenium-based test automation framework using Python. Whether you are new to Selenium or looking to create a simple yet effective automation framework, this project provides a foundation for your learning and development.

## Features

- **Selenium WebDriver:** Utilizes Selenium WebDriver to interact with web elements and automate browser actions.
- **Page Object Model (POM):** Implements the Page Object Model design pattern to enhance code maintainability and reusability.
- **Configuration:** Uses a configuration file for easy management of settings such as browser type and test URLs.
- **Sample Tests:** Includes sample test scripts to demonstrate how to create and run automated tests.
- **Logging:** Integrates logging to capture and report test execution details.
- **Requirements:** Lists project dependencies to ensure a smooth setup.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Selenium WebDriver
- Browser driver (e.g., ChromeDriver for Google Chrome)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/my-first-selenium-python-framework.git
    cd my-first-selenium-python-framework
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the appropriate browser driver and place it in the project's `drivers` directory.

4. Configure settings in the `config.ini` file:

    ```ini
    [WebDriver]
    browser = chrome  # or firefox, edge, etc.

    [TestURLs]
    base_url = https://example.com
    ```

## Running Tests

Execute the sample test script:

```bash
pytest -v -s --browser <browser_name> --url <website_URL>
```

## Contribution

Feel free to contribute to this project by:

1. Forking the repository
2. Creating a new branch (`git checkout -b feature/new-feature`)
3. Making your changes
4. Committing your changes (`git commit -m 'Add new feature'`)
5. Pushing to the branch (`git push origin feature/new-feature`)
6. Creating a pull request

## Issues

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/Ashuu11/my-first-selenium-python-framework-project/issues).

Happy testing!
