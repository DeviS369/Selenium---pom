import pytest
from pages.search_page import SearchPage
from utils.browser import get_browser

@pytest.fixture
def browser():
    driver = get_browser()
    yield driver
    driver.quit()

def test_imdb_search(browser):
    # Arrange
    search_page = SearchPage(browser)
    search_page.load()

    # Act
    search_page.fill_name_field("Tom Hanks")
    search_page.select_gender('male')
    search_page.submit_search()
    
    """
    search_page.select_birth_month("7")  # Example: July
    search_page.select_birth_day("9")
    search_page.select_birth_year("1956")
    search_page.submit_search()
    """

    # Assert: Verify that the search result page loads successfully
    assert "Tom Hanks" in browser.page_source
