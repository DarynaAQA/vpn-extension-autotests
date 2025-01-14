# Planet VPN Automation Project

This project is designed to automate testing of the Planet VPN extension.
Testing for next browsers: chrome, firefox, edge...

## Description README.md

1.Project structure
2.Installing dependencies
3.ENV file contents
4.Run tests


## 1. Structure project

project-root/
│
├── base_classes/
│ └── driver.py # Basic Driver Methods
│ └── api_requests.py # API for QASE reports
│ └── decrypt_payload.py # Key for decrypting the response (“payload”) of some API requests of our VPN
│
│
├── Extension/
│ └── ... # Building the project
│
├── locators/
│ └── ... # Web element locators
│
├── pages/
│ └── ... # Main extension pages (Page Objects)
│
├── tests/
│ └── ... # Tests
│
├── conftest.py # Fixtures
├── requirements.txt # Project Dependencies
├── Dockerfile # Docker file
└── .env # Environment Variables

## 2. Installing dependencies

pip install -r requirements.txt
add to requirements.txt ONLY those libraries that are used in tests


## 3. Running tests

#To run tests for specific browser and country, use pytest. Simply execute the following command in the project's root directory:

pytest -s -v --browser="your browser" tests

#To run a specific test or test file, specify its path after the pytest command. For example:

pytest -s -v --browser="your browser" tests/test_file.py::Class::function


