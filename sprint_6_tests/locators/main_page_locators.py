from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = By.CLASS_NAME, 'App_CookieButton__3cvqF'

    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]'

    ORDER_BUTTON_HEADER = By.XPATH, './/button[@class="Button_Button__ra12g"]'
    ORDER_BUTTON_MAIN = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
