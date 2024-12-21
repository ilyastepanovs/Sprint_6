from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, './/input[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, './/input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_INPUT = By.XPATH, './/input[@placeholder="* Станция метро"]'
    METRO_STATION = By.XPATH, ".//button/div[text()='{}']"
    TELEPHONE_INPUT = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, './/button[text() = "Далее"]'

    CALENDAR_INPUT = By.XPATH, ".//div[text()={}]"
    DELIVERY_DATE = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    RENT_PERIOD_DROPDOWN = By.XPATH, ".//div[text()='{}']"
    RENT_PERIOD = [By.XPATH, ".//div[text() = '* Срок аренды']"]
    ORDER_BUTTON = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    YES_BUTTON = By.XPATH, './/button[text() = "Да"]'
    SHOW_STATUS_BUTTON = By.XPATH, './/button[text() = "Посмотреть статус"]'

    FOR_WHO_TITLE = By.XPATH, ".//div[text() = 'Для кого самокат']"
    ABOUT_RENT_TITLE = By.XPATH, ".//div[text() = 'Про аренду']"
    ORDER_PLACED_TITLE = By.XPATH, './/div[text() = "Заказ оформлен"]'




