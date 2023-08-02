from selene import Browser, Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def open_and_close_browser():
    #op
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()))
    browser = Browser(
        Config(
            driver=driver
        )
    )
    #114.0.5735.90
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield browser
    browser.close()