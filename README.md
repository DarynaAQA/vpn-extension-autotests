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

## 3.ENV file contents

#API_TOKEN="59386c802e6a6f5d87d3d70a44dff55d53ebfe2373035d22acde1d3d973a8c9f"
#KEY="lNPQHj5MS7Z81ocu4r3Iq6hQFPu0EcLRAcejIOFfRGg="
#FREE_EMAIL="darina.planetvpn-test1@gmail.com"
#FREE_PASSWORD="qprtXd6X2F"
#PREMIUM_EMAIL="darina.planetvpn@gmail.com"
#PREMIUM_PASSWORD="ABCzxc816&D1"
#GH_TOKEN=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 //needed to install geckodriver on firefox browser//


## 4. Running tests

#To run tests for specific browser and country, use pytest. Simply execute the following command in the project's root directory:

pytest -s -v --browser="your browser" tests

#To run a specific test or test file, specify its path after the pytest command. For example:

pytest -s -v --browser="your browser" tests/test_file.py::Class::function


