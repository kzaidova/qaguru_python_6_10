from selene import browser
import pytest

@pytest.fixture
def open_and_close_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    yield browser
    browser.close()
