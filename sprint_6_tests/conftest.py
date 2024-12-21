import pytest
from selenium import webdriver

from sprint_6_tests.locators.main_page_locators import MainPageLocators
from sprint_6_tests.pages.dzen_page import DzenPage
from sprint_6_tests.pages.header_page import HeaderPage
from sprint_6_tests.pages.main_page import MainPage
from sprint_6_tests.pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture(scope='function')
def header_page(driver):
    return HeaderPage(driver)

@pytest.fixture(scope='function')
def dzen_page(driver):
    return DzenPage(driver)