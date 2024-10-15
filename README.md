# IMDb Search Automation

This project automates the search functionality on IMDb's "Search Name" page using Selenium WebDriver and Pytest. It follows the **Page Object Model (POM)** design pattern and uses **Explicit Wait** and **Expected Conditions** to interact with elements on the webpage.

## Project Structure
imdb_search/
│
├── pages/
│   └── search_page.py
├── tests/
│   └── test_search.py
├── utils/
│   └── browser.py
├── pytest.ini
└── requirements.txt


## Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver for Selenium (Managed automatically using `webdriver_manager`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/imdb-search-automation.git
   cd imdb-search-automation
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
pytest tests/test_search.py



