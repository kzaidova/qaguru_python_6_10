from selene import browser
import pytest

@pytest.fixture
def open_and_close_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield browser
    browser.close()
