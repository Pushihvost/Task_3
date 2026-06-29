from selenium.webdriver.common.by import By

class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, "(//ul[@class='OrderFeed_list__OLh59']/li)[1]")
    ORDER_POPUP_DETAILS = (By.XPATH, ".//p[text() = 'Cостав']/ancestor::div[contains(@class, 'container__Wo2l')]")


    COUNTER_ORDER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    COUNTER_ORDER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

    



